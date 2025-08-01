from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.serializers import UserListSerializer
from apps.users.serializers.List_serializers import CustomTokenObtainPairSerializer
from apps.users.services.permissions import IsAdminUserCustom
from apps.users.services.services import get_user_list_service


class UserListView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request):
        users = get_user_list_service()
        serializer = UserListSerializer(users, many=True)
        return Response(serializer.data)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer