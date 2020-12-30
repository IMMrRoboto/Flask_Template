#! usr/bin/python
# coding: utf-8

from flask import Flask, request, render_template, flash

DEBUG = True

app = Flask(__name__)

@app.route("/")
def landing():
	
	return render_template("index.html")

@app.route("/example")
def example():
	variable = "lorem ipsum"

	return render_template("example.html", variable=variable)

if __name__ == "__main__":
	app.run(port=8989, debug=True)
