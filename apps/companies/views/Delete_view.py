from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.companies.services.services import delete_company_service
from apps.users.services.permissions import IsAdminUserCustom


class CompanyDeleteView(APIView):
    permission_classes = [IsAdminUserCustom]

    def delete(self, request, company_id):
        result = delete_company_service(company_id)
        if not result:
            return Response({"detail": "Harbiy qism topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Harbiy qism muvaffaqiyatli o'chirildi."}, status=status.HTTP_204_NO_CONTENT)
