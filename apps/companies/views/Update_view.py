from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.companies.serializers import CompanyDetailSerializer, CompanyUpdateSerializer
from apps.companies.services.services import get_company_by_id_service, update_company_service
from apps.users.services.permissions import IsAdminUserCustom


class CompanyUpdateView(APIView):
    permission_classes = [IsAdminUserCustom]

    def put(self, request, company_id):
        company = get_company_by_id_service(company_id)
        if not company:
            return Response({"detail": "Harbiy qism topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanyUpdateSerializer(company, data=request.data, partial=True)
        if serializer.is_valid():
            company = update_company_service(company, serializer.validated_data)
            return Response(CompanyDetailSerializer(company).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
