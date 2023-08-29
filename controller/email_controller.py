from __future__ import unicode_literals

from controller.common_namespace import CommonNamespace
from flask import request
from flask_restx import Resource
from model.param import Param
from service import *
from util.request_util import args

from config import EMAIL

NAME = "email"
api = CommonNamespace(
    NAME,
    description=NAME,
    params=[
        Param(
            "to",
            str,
            "to",
            EMAIL["EMAIL"],
            True,
        ),
        Param(
            "cc",
            str,
            "cc",
            EMAIL["EMAIL"],
            False,
        ),
        Param(
            "bcc",
            str,
            "bcc",
            EMAIL["EMAIL"],
            False,
        ),
        Param("subject", str, "subject", "[TEST] mail", True),
        Param("html", str, "html", None, False),
        Param("text", str, "text", "test", False),
    ],
)


@api.route("/v1/send")
class EmailController(Resource):
    @api.doc(parser=api.parser)
    def get(self):
        return self.send()

    @api.doc(body=api.body)
    def post(self):
        return self.send()

    @staticmethod
    def send():
        params = args(request)

        return EmailService.send(**{x.name: params.get(x.name) for x in api.params})
