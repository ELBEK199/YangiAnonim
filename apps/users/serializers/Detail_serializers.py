from rest_framework import serializers
from apps.users.models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'first_name',
            'last_name',
            'is_admin',
            'is_active',
            'date_joined',
        ]
