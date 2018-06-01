from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
#api = Api(app)

@app.route("/")
def hello():
	return "Hello"
#api.add_resource(User,"/test")

#if __name__ == '__main__':
app.run(port='5002')
