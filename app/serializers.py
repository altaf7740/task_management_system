from rest_framework import serializers
from rest_framework_jwt.settings import api_settings
from .models import Task
from django.contrib.auth import authenticate
from django.contrib.auth.models import User

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'


class CustomJWTSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(read_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")
        user = authenticate(username=username, password=password)
        if user is None:
            raise serializers.ValidationError("Invalid username/password")
        if not user.is_active:
            raise serializers.ValidationError("User account is disabled")
        payload = api_settings.JWT_PAYLOAD_HANDLER(user)
        jwt_token = api_settings.JWT_ENCODE_HANDLER(payload)
        data["token"] = jwt_token
        return data


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'password')
