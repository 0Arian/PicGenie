from flask import Flask, request, redirect
import twilio.twiml
import ai_client

app = Flask(__name__)

@app.route("/", methods=['POST'])
def picInfo():
	resp = twilio.twiml.Response()

	numImages = int(request.form["NumMedia"])
	if  numImages < 1:
		response.message("Please send only one image at a time.")
	elif numImages > 1:
		response.message("Please send an image.")
	else:
		message.body = ai_client.get_name_and_description(request.form['MediaUrl0'])

	print str(message.body)
	return str(resp)

if (__name__) == "__main__":
	app.run(debug=True)
