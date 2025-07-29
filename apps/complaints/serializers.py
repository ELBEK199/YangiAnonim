from rest_framework import serializers
from .models import Complaint, COMPLAINT_CHOICES


class ComplaintCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['company', 'complaint_type', 'custom_text']

    def validate(self, data):
        # Faqat "shaxsiy_fikr" uchun custom_text majburiy, boshqalar uchun bo‘sh bo‘lishi kerak
        if data['complaint_type'] == 'shaxsiy_fikr' and not data.get('custom_text'):
            raise serializers.ValidationError({'custom_text': 'Shaxsiy fikr maydoni to‘ldirilishi shart.'})
        if data['complaint_type'] != 'shaxsiy_fikr' and data.get('custom_text'):
            raise serializers.ValidationError({'custom_text': 'Faqat shaxsiy fikrda matn yoziladi.'})
        return data


class ComplaintListSerializer(serializers.ModelSerializer):
    complaint_type_display = serializers.CharField(source='get_complaint_type_display', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Complaint
        fields = [
            'id', 'company', 'company_name', 'complaint_type', 'complaint_type_display',
            'custom_text', 'created_at', 'is_viewed', 'is_resolved'
        ]


class ComplaintDetailSerializer(serializers.ModelSerializer):
    complaint_type_display = serializers.CharField(source='get_complaint_type_display', read_only=True)
    company_name = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model = Complaint
        fields = [
            'id', 'company', 'company_name', 'complaint_type', 'complaint_type_display',
            'custom_text', 'created_at', 'is_viewed', 'is_resolved'
        ]
