from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.serializers import UserDetailSerializer
from apps.users.services.permissions import IsAdminUserCustom
from apps.users.services.services import get_user_by_id_service


class UserDetailView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request, user_id):
        user = get_user_by_id_service(user_id)
        if not user:
            return Response({"detail": "Foydalanuvchi topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)