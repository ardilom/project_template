# django
from django.shortcuts import get_object_or_404

# models
from ..models import User

# rest
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# serializers
from ..serializers import (
    UserBasicSerializer,
    UserSerializer,
)


class UserAdminViewSet(viewsets.ModelViewSet):
    """
    Viewset related to users
    """
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def list(self, request):
        users = User.filter.filter(is_active=True)
        serializer = self.get_serializer(users, many=True)

        return Response({"user": serializer.data})

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, id=pk, is_active=True)
        serializer = self.get_serializer(user)

        return Response({"user": serializer.data})

    def destroy(self, request, pk=None):
        user = get_object_or_404(User, id=pk, is_active=True)
        user.is_active = False
        user.save()
        return Response({"message": "Usuario borrado exitosamente!"})


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserBasicSerializer
    permission_classes = [AllowAny]

    def list(self, request):
        users = User.filter.filter(is_active=True)
        serializer = self.get_serializer(users, many=True)

        return Response({"user": serializer.data})

    def retrieve(self, request, pk=None):
        user = get_object_or_404(User, id=pk, is_active=True)
        serializer = self.get_serializer(user)

        return Response({"user": serializer.data})