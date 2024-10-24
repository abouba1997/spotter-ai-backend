from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
import jwt
import os
from library.models import User


class JWTAuthentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')
        if not auth_header:
            return None

        try:
            token = auth_header.split(' ')[1]
            payload = jwt.decode(token, os.getenv(
                'ACCESS_TOKEN_SECRET'), algorithms=[os.getenv('ALGORITHM')])
        except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
            raise exceptions.AuthenticationFailed('Invalid or expired token')

        user = User.objects.filter(id=payload['id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        return (user, None)
