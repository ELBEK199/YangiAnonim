from rest_framework import serializers
from apps.companies.models import Company


class CompanyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'identifier', 'qr_expiry', 'is_qr_valid']


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'qr_expiry']
        extra_kwargs = {
            'qr_expiry': {'required': False}
        }


class CompanyDetailSerializer(serializers.ModelSerializer):
    qr_code = serializers.ImageField(read_only=True)
    identifier = serializers.UUIDField(read_only=True)
    is_qr_valid = serializers.BooleanField(read_only=True)

    class Meta:
        model = Company
        fields = ['id', 'name', 'identifier', 'qr_code', 'qr_expiry', 'is_qr_valid', 'created_at']


class CompanyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'qr_expiry']
