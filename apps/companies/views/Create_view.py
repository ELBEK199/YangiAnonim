from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from apps.companies.serializers import CompanyCreateSerializer, CompanyDetailSerializer
from apps.companies.services.services import create_company_service
from apps.users.services.permissions import IsAdminUserCustom


class CompanyCreateView(APIView):
    permission_classes = [IsAdminUserCustom]

    @swagger_auto_schema(request_body=CompanyCreateSerializer)
    def post(self, request):
        serializer = CompanyCreateSerializer(data=request.data)
        if serializer.is_valid():
            company = create_company_service(
                name=serializer.validated_data['name'],
                qr_expiry=serializer.validated_data.get('qr_expiry')
            )
            return Response(CompanyDetailSerializer(company).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
