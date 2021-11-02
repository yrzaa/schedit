from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.settings import api_settings

from users import models
from users import serializers
from users import permissions


class UsersViewSet(viewsets.ViewSet):
    #dummy viewset
    def list(self, request):
        an_example = ['a', 'b', 'c']
        return Response({'msg': 'Hello', 'an_example': an_example})


# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating user profiles'''
    serializer_class = serializers.CustomUserSerializer
    queryset = models.CustomUser.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile, )


class CustomUserLoginApiView(ObtainAuthToken):
    '''Handle creating user auth tokens'''
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })

class ApplicationsViewSet(viewsets.ModelViewSet):
    '''Handle creating and updating requests'''
    serializer_class = serializers.ApplicationsSerializer2
    queryset =  models.Application.objects.all()
    authentication_classes = ()
    permission_classes = ()
