from rest_framework import exceptions
import jwt
import datetime
import os


def create_access_token(user_id):
    return jwt.encode({
        'id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        'iat': datetime.datetime.utcnow()
    }, os.getenv('ACCESS_TOKEN_SECRET'), algorithm=os.getenv('ALGORITHM'))


def decode_access_token(token):
    try:
        payload = jwt.decode(token, os.getenv(
            'ACCESS_TOKEN_SECRET'), algorithms=[os.getenv('ALGORITHM')])
        return payload['id']
    except:
        raise exceptions.AuthenticationFailed(
            'Please log in again.')


def create_refresh_token(user_id):
    return jwt.encode({
        'id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
        'iat': datetime.datetime.utcnow()
    }, os.getenv('REFRESH_TOKEN_SECRET'), algorithm=os.getenv('ALGORITHM'))


def decode_refresh_token(token):
    try:
        payload = jwt.decode(token, os.getenv(
            'REFRESH_TOKEN_SECRET'), algorithms=[os.getenv('ALGORITHM')])
        return payload['id']
    except:
        raise exceptions.AuthenticationFailed(
            'Please log in again.')
