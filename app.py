from flask import Flask, Markup, render_template, request, redirect
import twilio.twiml
import ai_client
from random import randint
 
app = Flask(__name__)
labels = []; values = []; colors = []

@app.route("/index")
def render_graph():
	print values
	print labels
	print colors

   	return render_template('chart.html', set=zip(values, labels, colors))

@app.route("/", methods=['POST'])
def handle_message():
	
	response = twilio.twiml.Response()
	numImages = int(request.form["NumMedia"])

	if  numImages > 1:
		response.message("Please send only one image at a time.")
	elif numImages < 1:
		response.message("Please send an image.")
	else:
		with response.message() as message:
			guess = ai_client.get_name(request.form['MediaUrl0'])

			try:
				labelIndex = labels.index(guess)
				values[labelIndex] += 1
			except ValueError as e:
				labels.append(guess)
				values.append(1)
			colors.append('#%06X' % randint(0, 0xFFFFFF))
			
                        retString = "Your picture is most likely a %s. " % guess
			retString += ai_client.get_wikipedia_desc(guess)
			message.body = retString
	print labels
	print values
	return str(response)

if (__name__) == "__main__":
	app.run(debug=True, host='0.0.0.0', port=5000)
