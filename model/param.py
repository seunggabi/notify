from flask_restx import fields


class Param:
    def __init__(self, name, type, description, default, required):
        self.name = name
        self.type = type
        self.help = self.description = description
        self.default = default
        self.required = required

    def query(self):
        return {
            "name": self.name,
            "type": self.type,
            "help": self.help,
            "default": self.default,
            "required": self.required,
        }

    def body(self):
        return self.name, fields.String(
            **{
                "description": self.description,
                "default": self.default,
                "required": self.required,
            }
        )
