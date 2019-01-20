import json
import jwt
from functools import wraps
from flask_jwt_extended import *
from flask import jsonify
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
            return 'Unauthorized', 401
    return wrapper


def decodeJWT(res, secret):
    '''
    decode jwt based on given response and app configuration
    '''
    return jwt.decode(json.loads(res.content)['access_token'], secret, algorithms=['HS256'])
