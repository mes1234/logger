from flask import Flask, request,  Response
from flask_restful import Resource, Api
from datetime import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from datetime import datetime

from sqlCreateDB import Project, Item, User, Base

from objetSerialization import *

from flask_jwt_extended import *
from helpers.auth import *
import os


class VueFlask(Flask):
    jinja_options = Flask.jinja_options.copy()
    jinja_options.update(dict(
        block_start_string='(%',
        block_end_string='%)',
        variable_start_string='((',
        variable_end_string='))',
        comment_start_string='(#',
        comment_end_string='#)',
    ))


app = VueFlask(__name__)
api = Api(app)

app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
jwt = JWTManager(app)

engine = create_engine('sqlite:///dbStorage.db')
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))
session = db_session()

projectSchemaObj = ProjectSchema()
itemSchemaObj = ItemSchema()
userSchemaObj = UserSchema()


class ProjectsAPI(Resource):
    @jwt_required
    @checkUser
    def get(self):
        '''
        fetch whole list of projects and return it as json
        endpoint: /projects
        '''
        data = session.query(Project).all()
        result = list(map(lambda obj: projectSchemaObj.dump(obj).data, data))
        return result, 200

    @jwt_required
    @checkUser
    def put(self):
        '''
        add project
        endpoint /projects
        '''
        record = projectSchemaObj.load(request.form)
        newProject = Project(**record.data)
        session.add(newProject)
        session.commit()


class Logout(Resource):
    '''
    rout to log out user
    '''
    @jwt_required
    @checkUser
    def post(self):
        username = request.json.get('username', None)
        jwtUsername = get_jwt_identity()
        if username == jwtUsername:
            LOGGED_USERS.remove(username)
            print(LOGGED_USERS)
            return {"username": username}, 200
        else:
            return jsonify('Unauthorized'), 401


class Login(Resource):
    '''
    rout to log in user
    '''

    def post(self):
        username = request.json.get('username', None)
        password = request.json.get('password', None)
        if validateUser(username=username, password=password):
            # Identity can be any data that is json serializable
            access_token = create_access_token(identity=username)
            LOGGED_USERS.add(username)
            print(LOGGED_USERS)
            return {"access_token": access_token}
        else:
            return jsonify('Unauthorized'), 401


class ItemsAPI(Resource):
    @jwt_required
    @checkUser
    def get(self, project_id):
        '''
        fetch all items stored in project with project_id
        endpoint: /projetcs/{project_id:int}/items
        '''
        data = session.query(Item) \
            .filter(Item.project_id == project_id) \
            .all()
        res = list(map(lambda x: itemSchemaObj.dump(x)[0], data))
        return res, 200

    @jwt_required
    @checkUser
    def put(self, project_id):
        '''
        add item to project with id project_id
        endpoint: /projects/{project_id:int}/items
        '''
        record = itemSchemaObj.load(request.form)
        newItem = Item(**record.data)
        session.add(newItem)
        session.commit()


api.add_resource(ProjectsAPI, '/projects')
api.add_resource(ItemsAPI, '/projects/<int:project_id>/items')
api.add_resource(Login, '/login')
api.add_resource(Logout, '/logout')
