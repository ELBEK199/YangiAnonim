from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.companies.serializers.Detail_serializers import CompanyDetailSerializer
from apps.companies.services.services import get_company_by_id_service
from apps.users.services.permissions import IsAdminUserCustom


class CompanyDetailView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request, company_id):
        company = get_company_by_id_service(company_id)
        if not company:
            return Response({"detail": "Harbiy qism topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CompanyDetailSerializer(company)
        return Response(serializer.data)
