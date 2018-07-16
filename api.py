from flask import Flask
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
#api = Api(app)

<<<<<<< HEAD
=======
print __name__
>>>>>>> d0066f9765fc3c611c5ba58c3cbe2874e7ae5c88
@app.route("/")
def hello():
	return "Hello"
#api.add_resource(User,"/test")

#if __name__ == '__main__':
app.run(port='5002')
