from __future__ import unicode_literals

from controller.common_namespace import CommonNamespace
from flask import request
from flask_restx import Resource
from model.param import Param
from service import *
from util.request_util import args

NAME = "slack"
api = CommonNamespace(
    NAME,
    description=NAME,
    params=[
        Param("message", str, "message", "test", False),
        Param("channel", str, "channel", None, False),
        Param("image", str, "image url", None, False),
        Param("test", str, "test", "true", False),
        Param("token", str, "token", SLACK["TOKEN"], False),
    ],
)


@api.route("/v1/send")
class SlackController(Resource):
    @api.doc(parser=api.parser)
    def get(self):
        return self.send()

    @api.doc(body=api.body)
    def post(self):
        return self.send()

    @staticmethod
    def send():
        params = args(request)

        return SlackService.send(**{x.name: params.get(x.name) for x in api.params})
