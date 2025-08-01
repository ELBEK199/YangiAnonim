from apps.complaints.models import Complaint, COMPLAINT_CHOICES
from django.db.models import Count, Q


def parse_period(period=None, from_date=None, to_date=None):
    q = Q()
    if from_date and to_date:
        q &= Q(created_at__date__gte=from_date, created_at__date__lte=to_date)
    return q


def get_stats_by_type(period=None, from_date=None, to_date=None):
    q = parse_period(period, from_date, to_date)
    # Bu yerda values() + annotate, natija: dict bo'ladi
    result = Complaint.objects.filter(q).values('complaint_type').annotate(count=Count('id'))
    complaint_type_map = dict(COMPLAINT_CHOICES)
    return [
        {
            'type': r['complaint_type'],
            'label': complaint_type_map.get(r['complaint_type'], r['complaint_type']),
            'count': r['count']
        }
        for r in result
    ]


def get_stats_by_company(period=None, from_date=None, to_date=None):
    q = parse_period(period, from_date, to_date)
    # values() ishlatiladi
    result = Complaint.objects.filter(q).values('company__id', 'company__name').annotate(count=Count('id'))
    return [
        {
            'company_id': r['company__id'],
            'company_name': r['company__name'],
            'count': r['count']
        }
        for r in result
    ]


def get_complaints_filtered(complaint_type=None, company_id=None, period=None, from_date=None, to_date=None):
    q = parse_period(period, from_date, to_date)
    if complaint_type:
        q &= Q(complaint_type=complaint_type)
    if company_id:
        q &= Q(company__id=company_id)
    # Bu return qilinayotgan natija Complaint object bo'ladi
    return Complaint.objects.filter(q).order_by('-created_at')
