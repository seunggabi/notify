from flask_restx import reqparse, Namespace


class CommonNamespace(Namespace):
    def __init__(self, name, params, **kwargs):
        super().__init__(name, **kwargs)
        self.params = params

        self.parser = reqparse.RequestParser()

        obj = {}
        for m in params:
            self.parser.add_argument(**m.query())

            k, v = m.body()
            obj[k] = v

        self.body = self.model(name, obj)
