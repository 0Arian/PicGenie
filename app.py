from flask import Flask, request, redirect
import twilio.twiml
import ai_client
import urllib

app = Flask(__name__)

@app.route("/", methods=['POST'])
def sms():
	
	response = twilio.twiml.Response()
	numImages = int(request.form["NumMedia"])

	if  numImages < 1:
		response.message("Please send only one image at a time.")
	elif numImages > 1:
		response.message("Please send an image.")
	else:
		with response.message() as message:
			message.media(request.form['MediaUrl0'])
			message.body = ai_client.get_name_and_description(request.form['MediaUrl0'])

	return str(response)

if (__name__) == "__main__":
	app.run(debug=True)
