from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.users.serializers import UserCreateSerializer, UserDetailSerializer
from apps.users.services.permissions import IsAdminUserCustom
from apps.users.services.services import get_user_by_id_service, update_user_service


class UserUpdateView(APIView):
    permission_classes = [IsAdminUserCustom]

    def put(self, request, user_id):
        user = get_user_by_id_service(user_id)
        if not user:
            return Response({"detail": "Foydalanuvchi topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserCreateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = update_user_service(user, serializer.validated_data)
            return Response(UserDetailSerializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)