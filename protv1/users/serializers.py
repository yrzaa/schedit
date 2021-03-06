from django.db.models import fields
from rest_framework import serializers
from users import models

class ApplicationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Application
        fields = ('certificate', 'slot', 'status', 'collected', 'delayed',)

class CustomUserSerializer(serializers.ModelSerializer):
    '''serializes a CustomUser profile object'''
    application_set = ApplicationsSerializer(many=True, read_only=True)
    
    class Meta:
        model = models.CustomUser
        fields = ('id', 'email', 'name', 'application_set', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }
    
    def create(self, validated_data):
        '''create and return a new user'''
        user = models.CustomUser.objects.create_user(
            email = validated_data['email'],
            name = validated_data['name'],
            password = validated_data['password']
        )
        return user



