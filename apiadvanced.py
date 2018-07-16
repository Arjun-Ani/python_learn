from flask import Flask, request
from flask_restful import Api, Resource, reqparse
from json import dumps
#from flask.ext.jsonpify import jsonify
from flask import jsonify
import MySQLdb


app = Flask(__name__)
api = Api(app)

class Add(Resource):
	def get(self):
		ip = request.args.get('ip')
		db = MySQLdb.connect("localhost","root","@19135nm","test")
		cursor = db.cursor()
		sql="INSERT INTO `test` (test) VALUES (%s);" %ip
		sql1="SELECT test FROM test;"
		cursor.execute(sql)
		db.commit()
		cursor.execute(sql1)
		db.commit()
		data = cursor.fetchall()
		db.close()
		return jsonify(data)


class Delete(Resource):
        def get(self):
                ip = request.args.get('ip')
                db = MySQLdb.connect("localhost","root","@19135nm","test")
                cursor = db.cursor()
                sql="DELETE FROM `test` WHERE test=%s;" %ip
                sql1="SELECT test FROM test;"
                cursor.execute(sql)
                db.commit()
                cursor.execute(sql1)
                db.commit()
                data = cursor.fetchall()
                db.close()
                return jsonify(data)



class List(Resource):
        def get(self):
                #ip = request.args.get('ip')
                db = MySQLdb.connect("localhost","root","@19135nm","test")
                cursor = db.cursor()
                #sql="DELETE FROM `test` WHERE test=%s;" %ip
                sql="SELECT test FROM test;"
                cursor.execute(sql)
                db.commit()
                #cursor.execute(sql1)
                #db.commit()
                data = cursor.fetchall()
                db.close()
                return jsonify(data)



api.add_resource(Add,'/add')
api.add_resource(Delete,'/delete')
api.add_resource(List,'/list')
app.run(debug=True ,port='5002')
