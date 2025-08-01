from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    UserListSerializer,
    UserCreateSerializer,
    UserDetailSerializer,
    CustomTokenObtainPairSerializer
)
from apps.users.services.permissions import IsAdminUserCustom
from apps.users.services.services import (
    create_user_service,
    update_user_service,
    delete_user_service,
    get_user_by_id_service,
    get_user_list_service
)
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


# User ro‘yxati va yaratish (GET, POST)
class UserListCreateView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request):
        users = get_user_list_service()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid():
            user = create_user_service(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password'],
                first_name=serializer.validated_data.get('first_name', ''),
                last_name=serializer.validated_data.get('last_name', ''),
                is_admin=serializer.validated_data.get('is_admin', False),
                is_active=serializer.validated_data.get('is_active', True)
            )
            return Response(UserDetailSerializer(user).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# User detail, update, delete (GET, PUT/PATCH, DELETE)
class UserDetailUpdateDeleteView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request, user_id):
        user = get_user_by_id_service(user_id)
        if not user:
            return Response({"detail": "Foydalanuvchi topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserDetailSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id):
        user = get_user_by_id_service(user_id)
        if not user:
            return Response({"detail": "Foydalanuvchi topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        serializer = UserCreateSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            user = update_user_service(user, serializer.validated_data)
            return Response(UserDetailSerializer(user).data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        result = delete_user_service(user_id)
        if not result:
            return Response({"detail": "Foydalanuvchi topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Foydalanuvchi muvaffaqiyatli o'chirildi"}, status=status.HTTP_204_NO_CONTENT)
