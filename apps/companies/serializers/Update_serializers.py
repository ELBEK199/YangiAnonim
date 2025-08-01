from rest_framework import serializers
from apps.companies.models import Company


class CompanyUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['name', 'qr_expiry']
