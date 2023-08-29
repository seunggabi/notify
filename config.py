from util.core_util import getenv_default

PORT = getenv_default("PORT") or "80"
HOST = getenv_default("HOST") or "0.0.0.0"
PROTOCOL = getenv_default("PROTOCOL") or "http"

PROFILE = getenv_default("PROFILE")
LEVEL = "INFO" if PROFILE.lower() == "local" else "ERROR"

EMAIL = {
    "DOMAIN": getenv_default("EMAIL_DOMAIN"),
    "SERVER": getenv_default("EMAIL_SERVER"),
    "PORT": getenv_default("EMAIL_PORT"),
    "NAME": getenv_default("EMAIL_NAME"),
    "EMAIL": getenv_default("EMAIL"),
}
EMAIL["EMAIL"] = EMAIL["NAME"] + "@" + EMAIL["DOMAIN"]
EMAIL["FROM"] = EMAIL["NAME"] + " <" + EMAIL["EMAIL"] + ">"

LOG = {
    "version": 1,
    "formatters": {
        "default": {
            "format":
                """{
                    "timestamp":"%(asctime)s",
                    "level":"%(levelname)s",
                    "logger":"%(module)s",
                    "message":"%(message)s"
                }""",
        }
    },
    "handlers": {
        "console": {
            "level": LEVEL,
            "class": "logging.StreamHandler",
            "formatter": "default",
        },
        "file": {
            "level": "INFO",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "filename": "log/bot.log",
            "when": "midnight",
            "backupCount": 15,
            "formatter": "default",
        },
    },
    "root": {
        "level": "INFO",
        "handlers": ["console", "file"],
    },
}

SLACK = {
    "TOKEN": getenv_default("SLACK_TOKEN"),
    "CHANNEL": getenv_default("SLACK_CHANNEL"),
    "CHANNEL_TEST": getenv_default("SLACK_CHANNEL_TEST"),
}
