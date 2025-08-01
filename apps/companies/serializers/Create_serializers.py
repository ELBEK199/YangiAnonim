from rest_framework import serializers
from apps.companies.models import Company


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'qr_expiry']
        extra_kwargs = {
            'qr_expiry': {'required': False}
        }
