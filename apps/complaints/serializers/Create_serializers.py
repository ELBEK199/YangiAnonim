from rest_framework import serializers
from apps.complaints.models import Complaint


class ComplaintCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ['company', 'complaint_type', 'custom_text']

    def validate(self, data):
        if data['complaint_type'] == 'shaxsiy_fikr' and not data.get('custom_text'): #Faqat shaxsiyfikrda textarea chiqadi.
            raise serializers.ValidationError({'custom_text': 'Shaxsiy fikr maydoni to‘ldirilishi shart.'})
        if data['complaint_type'] != 'shaxsiy_fikr' and data.get('custom_text'):
            raise serializers.ValidationError({'custom_text': 'Faqat shaxsiy fikrda matn yoziladi.'})
        return data
