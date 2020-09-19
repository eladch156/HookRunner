from flask import Flask, render_template, request
from flask_restful import Api,Resource
from WebClient.Application.Client import Client
import atexit

App = Flask(__name__)
Api = Api(App)

@App.before_first_request
def job():
    global CLIENT
    CLIENT = Client()

@App.route("/")
def index():
    return render_template("index.html")

class Hook(Resource):
    def post(self):
        global CLIENT
        json = request.json
        CLIENT.send(json)

Api.add_resource(Hook, "/hook")

if __name__ == "__main__":
    App.run(debug=True)