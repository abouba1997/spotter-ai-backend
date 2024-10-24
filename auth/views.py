from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.db.models import Q
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.authentication import get_authorization_header
from .serializers import UserSerializer
from library.models import User
from .authentication import JWTAuthentication
from .tokens import create_access_token, create_refresh_token, decode_access_token, decode_refresh_token


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Registration successfully'}, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        user = None
        email = request.data.get('email')

        user = User.objects.filter(email=email).first()

        if user and user.check_password(request.data['password']):
            access_token = create_access_token(user.id)
            refresh_token = create_refresh_token(user.id)

            response = Response()

            response.set_cookie(key='refresh_token',
                                value=refresh_token, httponly=True)

            response.data = {
                'token': access_token,
                'user': UserSerializer(user).data
            }
            response.status_code = status.HTTP_200_OK

            return response
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        auth_value = get_authorization_header(request).split()

        if auth_value and len(auth_value) == 2:
            token = auth_value[1].decode('utf-8')
            user_id = decode_access_token(token)
            user = User.objects.filter(pk=user_id).first()
            serializer = UserSerializer(user)
            return Response(serializer.data)

        raise AuthenticationFailed('Unauthenticated. Please log in.')


class RefreshTokenView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        print(request.COOKIES)
        refresfh_token = request.COOKIES.get('refresh_token')
        if not refresfh_token:
            raise AuthenticationFailed('Refresh token required.')

        user_id = decode_refresh_token(refresfh_token)
        access_token = create_access_token(user_id)
        print(user_id)
        print(access_token)
        user = User.objects.filter(pk=user_id).first()
        serializer = UserSerializer(user)
        return Response({'token': access_token, 'user': serializer.data})


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        response = Response()
        response.delete_cookie(key='refresh_token')
        response.data = {
            'message': 'success'
        }

        return response
