# models
from ..models import Notification

# serializers
from . import IsActiveListSerializer

# rest framework
from rest_framework import serializers


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        list_serializer_class = IsActiveListSerializer
        model = Notification
        fields = '__all__'
        depth = 1
