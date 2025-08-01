from rest_framework import status
from rest_framework.views import APIView
from apps.users.serializers import UserCreateSerializer, UserDetailSerializer
from apps.users.services.permissions import IsAdminUserCustom
from apps.users.services.services import create_user_service
from rest_framework.response import Response


class UserCreateView(APIView):
    permission_classes = [IsAdminUserCustom]

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
