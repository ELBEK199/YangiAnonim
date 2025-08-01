from rest_framework.response import Response
from rest_framework.views import APIView
from apps.complaints.models import COMPLAINT_CHOICES


class ComplaintTypesView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        types = [
            {"value": value, "label": label}
            for value, label in COMPLAINT_CHOICES
        ]
        return Response(types)
