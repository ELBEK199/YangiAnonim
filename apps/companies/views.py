from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    CompanyListSerializer,
    CompanyCreateSerializer,
    CompanyDetailSerializer,
    CompanyUpdateSerializer
)
from org_survey.users.permissions import IsAdminUserCustom
from org_survey.companies.services import (
    create_company_service,
    update_company_service,
    delete_company_service,
    get_company_by_id_service,
    get_company_list_service
)
from drf_yasg.utils import swagger_auto_schema


class CompanyListCreateView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request):
        companies = get_company_list_service()
        serializer = CompanyListSerializer(companies, many=True)
        return Response(serializer.data)

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


class CompanyDetailUpdateDeleteView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request, company_id):
        company = get_company_by_id_service(company_id)
        if not company:
            return Response({"detail": "Harbiy qism topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanyDetailSerializer(company)
        return Response(serializer.data)

    def put(self, request, company_id):
        company = get_company_by_id_service(company_id)
        if not company:
            return Response({"detail": "Harbiy qism topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanyUpdateSerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            company = update_company_service(company, serializer.validated_data)
            return Response(CompanyDetailSerializer(company).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, company_id):
        result = delete_company_service(company_id)
        if not result:
            return Response({"detail": "Harbiy qism topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Harbiy qism muvaffaqiyatli o'chirildi."}, status=status.HTTP_204_NO_CONTENT)
