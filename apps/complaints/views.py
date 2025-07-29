from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    ComplaintCreateSerializer,
    ComplaintListSerializer,
    ComplaintDetailSerializer
)
from apps.complaints.models import COMPLAINT_CHOICES
from org_survey.users.permissions import IsAdminUserCustom  # adminlar uchun permission
from org_survey.complaints.services import (
    create_complaint_service,
    get_complaint_list_service,
    get_complaint_by_id_service,
    mark_complaint_viewed_service,
    mark_complaint_resolved_service,
    delete_complaint_service
)
from apps.companies.models import Company
from drf_yasg.utils import swagger_auto_schema

# 1. Murojaat yuborish (public, login talab qilmaydi, faqat QR orqali frontdan chaqiriladi)
class ComplaintCreateView(APIView):
    authentication_classes = []  # Anonymous allowed (login talab qilinmaydi)
    permission_classes = []  # Qo'shimcha xavfsizlik uchun token/QR check frontendda

    @swagger_auto_schema(request_body=ComplaintCreateSerializer)
    def post(self, request):
        serializer = ComplaintCreateSerializer(data=request.data)
        if serializer.is_valid():
            # Kompaniyani id yoki token orqali olish (frontend POSTda yuboradi)
            company_id = serializer.validated_data['company'].id
            company = Company.objects.filter(id=company_id).first()
            if not company:
                return Response({'detail': 'Harbiy qism topilmadi.'}, status=status.HTTP_404_NOT_FOUND)
            complaint = create_complaint_service(
                company=company,
                complaint_type=serializer.validated_data['complaint_type'],
                custom_text=serializer.validated_data.get('custom_text', '')
            )
            return Response(ComplaintDetailSerializer(complaint).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 2. Admin uchun murojaatlar ro‘yxati va detail (login required)
class ComplaintListView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request):
        complaints = get_complaint_list_service()
        serializer = ComplaintListSerializer(complaints, many=True)
        return Response(serializer.data)


class ComplaintDetailView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request, complaint_id):
        complaint = get_complaint_by_id_service(complaint_id)
        if not complaint:
            return Response({"detail": "Harbiy qism topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ComplaintDetailSerializer(complaint)
        return Response(serializer.data)

    def patch(self, request, complaint_id):
        complaint = get_complaint_by_id_service(complaint_id)
        if not complaint:
            return Response({"detail": "Harbiy qism topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        action = request.data.get('action')
        if action == 'viewed':
            mark_complaint_viewed_service(complaint)
        elif action == 'resolved':
            mark_complaint_resolved_service(complaint)
        serializer = ComplaintDetailSerializer(complaint)
        return Response(serializer.data)

    def delete(self, request, complaint_id):
        result = delete_complaint_service(complaint_id)
        if not result:
            return Response({"detail": "Harbiy qism topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Harbiy qism muvaffaqiyatli o'chirildi."}, status=status.HTTP_204_NO_CONTENT)

class ComplaintTypesView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        types = [
            {"value": value, "label": label}
            for value, label in COMPLAINT_CHOICES
        ]
        return Response(types)
