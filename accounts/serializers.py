from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()
from .models import UserAccount

class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer):
        model = User
        fields = ('id', 'email', 'name', 'password')

class UserlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('id','name','email',)