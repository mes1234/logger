from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime

from sqlCreateDB import Project, Item, User, Base

from objetSerialization import *


app = Flask(__name__)
api = Api(app)

engine = create_engine('sqlite:///dbStorage.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
session = db_session()

s = ProjectSchema()
i = ItemSchema()


class ProjectsAPI(Resource):
    def get(self):
        data = session.query(Project).all()
        res = s.dump(data[0])
        return res[0], 200


class ItemsAPI(Resource):
    def get(self, project_id):
        data = session.query(Item) \
            .filter(Item.project_id == project_id) \
            .all()
        res = list(map(lambda x: i.dump(x)[0], data))
        return res, 200


api.add_resource(ProjectsAPI, '/projects')
api.add_resource(ItemsAPI, '/projects/<int:project_id>/items')
# if __name__ == '__main__':
#     app.run(debug=True)
