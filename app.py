from flask import Flask,request
from flask_restful import Resource, Api
from datetime import datetime

app = Flask(__name__)
api = Api(app)

db = {
    1:{
        'data':str(datetime.now()),
        'project':'test1',
        'description':'desc1'
    },
    2:{
        'data':str(datetime.now()),
        'project':'test2',
        'description':'desc2'
    },
}

class List(Resource):
    def get(self):
        return db,200
class Add(Resource):
    def put(self):
        item =  {
            'data':str(datetime.now()),
            'project':'project',
            'description':request.form['description']
        }
        lenght=len(db)
        db.update({lenght+1:item})
        return item,200


api.add_resource(List,'/list:<string>')
api.add_resource(Add,'/add')

# if __name__ == '__main__':
#     app.run(debug=True)
	
	
	
