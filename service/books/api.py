from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Books(Resource):
    def get(self):
        return {
            "books": [
                "Think Python",
                "Fluent Python",
                "Effective Python: 59 Ways to Write Better Python",
                "Python Cookbook",
            ]
        }


api.add_resource(Books, "/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
