# django
from django.contrib.auth.models import User

# rest framework
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class UserRegisterSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField("get_user_token")

    def get_user_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj.user)
        return token.key

    class Meta:
        model = User


class UserBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("first_name", )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
