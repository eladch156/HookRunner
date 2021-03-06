from flask import Flask, render_template, request
from flask_restful import Api, Resource
from WebClient.Application.Client import Client
import atexit
import configparser
from pathlib import Path

# Specific For Flask! ####################
# Convention should not used globaly! ####
Config = configparser.ConfigParser()
CfgPath = (Path(__file__).parent / "web_client.ini").resolve().absolute()
Config.read(CfgPath)
App = Flask(__name__)
Api = Api(App)
#########################################


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
        _json = request.json
        if "Run" in _json:
            _hook_run_req = {
                "Name": "RunHook",
                "Data": {
                    "HookPath": str((
                        Path(Config["General"]["hooks_repository"])
                        / _json["Run"]).resolve().absolute())
                }
            }
            CLIENT.send(_hook_run_req)


Api.add_resource(Hook, "/hook")


if __name__ == "__main__":
    App.run(debug=True)
