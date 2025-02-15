from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Fruits(Resource):
    def get(self):
        return {
            "fruits": [
                "Apple",
                "Orange",
                "Melon",
                "Grapes",
            ]
        }


api.add_resource(Fruits, "/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
