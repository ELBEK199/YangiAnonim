from drf_yasg.utils import swagger_auto_schema
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.companies.models import Company
from apps.complaints.serializers import ComplaintCreateSerializer, ComplaintDetailSerializer
from apps.complaints.services.services import create_complaint_service


class ComplaintCreateView(APIView):
    authentication_classes = []
    permission_classes = []

    @swagger_auto_schema(request_body=ComplaintCreateSerializer)
    def post(self, request):
        serializer = ComplaintCreateSerializer(data=request.data)
        if serializer.is_valid():
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
