
# rest framework
from rest_framework import serializers


class IsActiveListSerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(is_active=True)
        return super(IsActiveListSerializer, self).to_representation(data)
