from __future__ import unicode_literals

from argparse import ArgumentParser
from flask import Flask, redirect
from flask_restx import Api
from logging.config import dictConfig
from werkzeug.exceptions import HTTPException, BadRequest, abort

from seunggabi_core_python.util import env_util
from const import TEST

from config import *
from controller import *

dictConfig(LOG)

app = Flask(__name__)


@app.errorhandler(Exception)
def handle_exception(e):
    if isinstance(e, HTTPException):
        return e

    if isinstance(e, KeyError):
        raise BadRequest(f"the field {e} not exist!")

    return abort(500)


@app.route("/")
def home():
    host = "0.0.0.0" if env_util.get("ENV") == TEST else HOST

    return redirect(f"{PROTOCOL}://{host}:{PORT}/swagger-ui.html")


@app.route("/actuator/health/liveness")
def liveness():
    return "health checked"


@app.route("/actuator/health/readiness")
def readiness():
    return "health checked"


api = Api(
    app, version="1.0", title="Bot API", description="Bot API", doc="/swagger-ui.html"
)

api.add_namespace(Slack)
api.add_namespace(Email)

if __name__ == "__main__":
    arg_parser = ArgumentParser(
        usage="Usage: python " + __file__ + " [--port <port>] [--help]"
    )
    arg_parser.add_argument("-p", "--port", default=PORT, help="port")
    arg_parser.add_argument("-d", "--debug", default=True, help="debug")
    options = arg_parser.parse_args()

    app.run(
        host="0.0.0.0",
        debug=options.debug,
        port=options.port,
    )
