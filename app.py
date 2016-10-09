from flask import Flask, request, redirect
import twilio.twiml
import ai_client
from PIL import Image


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
		file = Image.open(request.form['MediaUrl0'])
		message.body = ai_client.get_name_and_description(file)

	print str(message.body)
	return str(resp)

if (__name__) == "__main__":
	app.run(debug=True)
