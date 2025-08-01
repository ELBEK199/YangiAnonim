from rest_framework.views import APIView
from rest_framework.response import Response
from apps.complaints.serializers import ComplaintListSerializer
from apps.complaints.services.services import get_complaint_list_service
from apps.users.services.permissions import IsAdminUserCustom


class ComplaintListView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request):
        complaints = get_complaint_list_service()
        serializer = ComplaintListSerializer(complaints, many=True)
        return Response(serializer.data)
