from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Members


# Create your views here.

class AuthView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        content = {
            'username': username,
            "password": password
            }

        print(username)
        user = Members.objects.get(username=username)
        # user.id = user.member_id

        refresh = RefreshToken.for_user(user)

        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
        return Response(content)



class HelloView(APIView):
    permission_classes = (permissions.IsAuthenticated,)
    # permission_classes = (permissions.AllowAny,)

    def get(self, request):
        
        # usernames = [user.email for user in User.objects.all()]
        print(request.user.username)
        # return Response(usernames)
        content = {'message': 'Hello, World!'}
        return Response(content)


