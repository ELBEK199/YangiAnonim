from rest_framework import serializers
from apps.companies.models import Company


class CompanyDetailSerializer(serializers.ModelSerializer):
    qr_code = serializers.ImageField(read_only=True)
    identifier = serializers.UUIDField(read_only=True)
    is_qr_valid = serializers.ReadOnlyField()

    class Meta:
        model = Company
        fields = ['id', 'name', 'identifier', 'qr_code', 'qr_expiry', 'is_qr_valid', 'created_at']
