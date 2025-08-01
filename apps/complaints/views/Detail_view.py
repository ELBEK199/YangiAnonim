from rest_framework.response import Response
from rest_framework.views import APIView
from apps.complaints.serializers import ComplaintDetailSerializer
from apps.complaints.services.services import get_complaint_by_id_service, mark_complaint_viewed_service, \
    mark_complaint_resolved_service, delete_complaint_service
from apps.users.services.permissions import IsAdminUserCustom
from rest_framework import status

class ComplaintDetailView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request, complaint_id):
        complaint = get_complaint_by_id_service(complaint_id)
        if not complaint:
            return Response({"detail": "Harbiy qism topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        serializer = ComplaintDetailSerializer(complaint)
        return Response(serializer.data)

    def patch(self, request, complaint_id):
        complaint = get_complaint_by_id_service(complaint_id)
        if not complaint:
            return Response({"detail": "Harbiy qism topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        action = request.data.get('action')
        if action == 'viewed':
            mark_complaint_viewed_service(complaint)
        elif action == 'resolved':
            mark_complaint_resolved_service(complaint)
        serializer = ComplaintDetailSerializer(complaint)
        return Response(serializer.data)

    def delete(self, request, complaint_id):
        result = delete_complaint_service(complaint_id)
        if not result:
            return Response({"detail": "Harbiy qism topilmadi."}, status=status.HTTP_404_NOT_FOUND)
        return Response({"detail": "Harbiy qism muvaffaqiyatli o'chirildi."}, status=status.HTTP_204_NO_CONTENT)
