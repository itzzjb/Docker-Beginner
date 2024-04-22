# Basic flask python file 
# This file will be used to create a simple flask app that will be deployed on the server

from flask import Flask
helloworld = Flask(__name__)
@helloworld.route("/")
def run():
    return "{\"message\":\"Hey there python\"}"

if __name__ == "__main__":
    helloworld.run(host="0.0.0.0", port=int("3000"), debug=True)