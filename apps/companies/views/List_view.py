from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from apps.companies.models import Company
from apps.companies.serializers.List_serializers import CompanyListSerializer
from apps.users.services.permissions import IsAdminUserCustom


class CompanyListView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request):
        companies = Company.objects.all().order_by('-created_at')
        serializer = CompanyListSerializer(companies, many=True)  # to'g'ri serializer
        return Response(serializer.data, status=status.HTTP_200_OK)
