from rest_framework import serializers

from apps.complaints.models import Complaint


class ComplaintListSerializer(serializers.ModelSerializer):
    complaint_type_display = serializers.CharField(source='get_complaint_type_display', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Complaint
        fields = [
            'id', 'company', 'company_name', 'complaint_type', 'complaint_type_display',
            'custom_text', 'created_at', 'is_viewed', 'is_resolved'
        ]
