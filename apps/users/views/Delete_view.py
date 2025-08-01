from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.services.permissions import IsAdminUserCustom
from apps.users.services.services import delete_user_service


class UserDeleteView(APIView):
    permission_classes = [IsAdminUserCustom]

    def delete(self, request, user_id):
        result = delete_user_service(user_id)
        if not result:
            return Response({"detail": "Foydalanuvchi topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Foydalanuvchi muvaffaqiyatli o'chirildi"}, status=status.HTTP_204_NO_CONTENT)
