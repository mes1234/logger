import requests
import pytest
import jwt
import json
import os
from auth import *

TOKEN_SAVE = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE1NDgxMDY5NjksIm5iZiI6MTU0ODEwNjk2OSwianRpIjoiZTA0MjVhNDQtMjk5YS00YzRkLTk5ZWQtNmNjMTAyZGRiMDY1IiwiZXhwIjoxNTQ4MTA3ODY5LCJpZGVudGl0eSI6MSwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.Qw4k9s12LYJqy8Od6ieSayvPzTysPVCCO3BMj9ydWn4'


@pytest.fixture
def auth_preproc():
    '''
    setup of test requiring token prior
    '''
    print(os.environ['JWT_SECRET_KEY'])
    res = requests.post(url='http://127.0.0.1:5000/login', json={
        'username': 'Witek',
        'password': '1234',
    })
    token = json.loads(res.content)['access_token']
    res = {}
    res.update({
        'token': token
    })
    return res


def test_LoginRoute():
    '''
    verify if loggin in works
    '''
    res = requests.post(url='http://127.0.0.1:5000/login', json={
        'username': 'Witek',
        'password': '1234',
    })
    assert decodeJWT(res, os.environ['JWT_SECRET_KEY'])['identity'] == 1


def test_LoginRouteFalsePassword():
    '''
    verify if loggin in works
    '''
    res = requests.post(url='http://127.0.0.1:5000/login', json={
        'username': 'Witek',
        'password': '1234232',
    })
    assert json.loads(res.text) == 'Unauthorized'


def test_LogoutRoute(auth_preproc):
    '''
    verify if logout works
    '''
    token = auth_preproc['token']
    header = {
        'Authorization': f'Bearer {token}'
    }
    res = requests.get(url='http://127.0.0.1:5000/logout', headers=header)
    print(res)
    assert json.loads(res.text) == 'Logout Successful'


# def test_LogoutRouteFalseToken(auth_preproc):
#     '''
#     verify if logout works
#     #FIXME this functionality is not protected from reusing token!!
#     '''
#     token = auth_preproc['token']
#     token = TOKEN_SAVE
#     header = {
#         'Authorization': f'Bearer {token}'
#     }
#     res = requests.get(url='http://127.0.0.1:5000/logout', headers=header)
#     print(res)
#     assert json.loads(res.text) == 'Unauthorized'


def test_FetchProjectsList(auth_preproc):
    '''
    check fetching project list from server
    '''
    token = auth_preproc['token']
    header = {
        'Authorization': f'Bearer {token}'
    }
    res = requests.get(url='http://127.0.0.1:5000/projects', headers=header)
    assert res.status_code == 200


def test_FetchProjectsListNoHeader(auth_preproc):
    '''
    check fetching project list from server
    '''
    token = auth_preproc['token']
    header = {
        'Authorization': f'Bearer {token}'
    }
    res = requests.get(url='http://127.0.0.1:5000/projects')
    assert res.status_code == 500
