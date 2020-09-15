from rest_framework import HTTP_HEADER_ENCODING, authentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.models import Members
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.exceptions import InvalidToken, AuthenticationFailed
from django.utils.translation import gettext_lazy as _


from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User

# from customers.models import Customer

class MemberBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        print("asdf")
        customer_id = kwargs['username']
        password = kwargs['password']
        try:
            # member = Members.objects.get(username=customer_id)
            print("==1")
            member = Members.objects.filter(username=customer_id).first()
            print("==2")
            print(member)
            print("==3")
            member.id = member.member_id
            print("==4")
            print(member.password, )
            # if member.check_password(password) is True:
            if member.password == password:
                member.is_active = True
                return member
        except Members.DoesNotExist:
            pass



class CustomAuthBackend(JWTAuthentication):
    # def authenticate(self, request):
    #     print('hii')
    #     return True

        def get_user(self, validated_token):
            print(validated_token,"===============")
            """
            Attempts to find and return a user using the given validated token.
            """
            try:
                user_id = validated_token[api_settings.USER_ID_CLAIM]
                print("user_id = ", user_id)
            except KeyError:
                raise InvalidToken(_('Token contained no recognizable user identification'))

            try:
                user = Members.objects.get(**{api_settings.USER_ID_FIELD: user_id})
            except Members.DoesNotExist:
                raise AuthenticationFailed(_('User not found'), code='user_not_found')

            # if not user.is_active:
            #     raise AuthenticationFailed(_('User is inactive'), code='user_inactive')

            # user=Members.objects.first()
            # user.is_authenticated= True
            return user


