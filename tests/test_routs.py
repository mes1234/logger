import requests
import pytest
import jwt
import json
import os
from helpers.auth import *
from flask_jwt_extended import *


@pytest.fixture(scope='session')
def auth_preproc():
    '''
    setup of test requiring token prior
    '''
    print(os.environ['JWT_SECRET_KEY'])
    res = requests.post(url='http://127.0.0.1:5000/login', json={
        'username': 'witek',
        'password': '1234',
    })
    token = json.loads(res.content)['access_token']
    res = {}
    res.update({
        'token': token
    })
    return res


def test_LoginRoute(auth_preproc):
    '''
    verify if loggin in works
    '''
    res = requests.post(url='http://127.0.0.1:5000/login', json={
        'username': 'witek',
        'password': '1234',
    })
    assert decodeJWT(res, os.environ['JWT_SECRET_KEY'])['identity'] == 'witek'


def test_LogoutRoute(auth_preproc):
    '''
    verify if logout works
    '''
    token = auth_preproc['token']
    header = {
        'Authorization': f'Bearer {token}'
    }
    res = requests.post(url='http://127.0.0.1:5000/logout',
                        headers=header, json={'username': 'witek'})
    assert json.loads(res.text)['username'] == 'witek'
