from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import UserProfile,NetworkEdge


class UserCreateSerializer(ModelSerializer):

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data['password'])

        user = User.objects.create(**validated_data)

        UserProfile.objects.create(user=user)

        return user

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class UserViewSerializer(ModelSerializer):
    class Meta:
        model=User
        fields = ('first_name', 'last_name', 'email')

class UserProfileViewSerializer(ModelSerializer):
    user= UserViewSerializer()
    class Meta:
        model = UserProfile
        fields = ('bio', 'profile_pic_url', 'user')

class UserProfileUpdateSerializer(ModelSerializer):

    first_name=serializers.CharField()
    last_name=serializers.CharField()

    def update(self,instance, validated_data):

        user = instance.user

        user.first_name=validated_data.pop('first_name',None)
        user.last_name=validated_data.pop('last_name',None)

        user.save()

        instance.bio = validated_data.pop('bio',None)
        instance.profile_pic_url = validated_data.get('profile_pic_url', None)
        instance.save()

        return instance




    class Meta:
        model = UserProfile
        fields = ('bio','first_name','last_name','profile_pic_url')


class NetworkEdgeCreateSerializer(ModelSerializer):

    class Meta:
        model=NetworkEdge
        fields=('from_user','to_user')