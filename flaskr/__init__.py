from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello():
	ua = request.headers.get('User-Agent')
	if ua.startswith("curl"):
		return "You are in curl"
	return "You are in a browser (probably...)"
