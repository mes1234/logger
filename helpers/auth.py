import json
import jwt
from functools import wraps
from flask_jwt_extended import *
from flask import jsonify
USERS = {
    'witek': '1234',
}
LOGGED_USERS = set()


def checkUser(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        '''
        check if user exist in USERS pool
        '''
        current_user = get_jwt_identity()
        if current_user in LOGGED_USERS:
            return fn(*args, **kwargs)
        else:
            return jsonify("Unauthorized"), 401
    return wrapper


def validateUser(username: str, password: str):
    '''
    function to verify if valid user is signing in
    '''
    if username in USERS.keys():
        if password == USERS[username]:
            return True
        else:
            return False
    else:
        return False


def decodeJWT(res, secret):
    '''
    decode jwt based on given response and app configuration
    '''
    return jwt.decode(json.loads(res.content)['access_token'], secret, algorithms=['HS256'])
