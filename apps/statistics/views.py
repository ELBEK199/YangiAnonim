from rest_framework.views import APIView
from rest_framework.response import Response
from org_survey.static.services import (
    get_stats_by_type,
    get_stats_by_company,
    get_complaints_filtered,
)
from apps.complaints.serializers import ComplaintListSerializer
from org_survey.users.permissions import IsAdminUserCustom  # faqat admin uchun


class StatsByTypeView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request):
        period = request.GET.get('period')  # 'month', 'week', 'year'
        from_date = request.GET.get('from')
        to_date = request.GET.get('to')
        data = get_stats_by_type(period, from_date, to_date)
        return Response(data)


class StatsByCompanyView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request):
        period = request.GET.get('period')
        from_date = request.GET.get('from')
        to_date = request.GET.get('to')
        data = get_stats_by_company(period, from_date, to_date)
        return Response(data)


class ComplaintsFilteredView(APIView):
    permission_classes = [IsAdminUserCustom]

    def get(self, request):
        complaint_type = request.GET.get('type')
        company_id = request.GET.get('company_id')
        period = request.GET.get('period')
        from_date = request.GET.get('from')
        to_date = request.GET.get('to')
        queryset = get_complaints_filtered(complaint_type, company_id, period, from_date, to_date)
        serializer = ComplaintListSerializer(queryset, many=True)
        return Response(serializer.data)
