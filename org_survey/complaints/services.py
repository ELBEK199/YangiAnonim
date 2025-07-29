from apps.complaints.models import Complaint
from apps.companies.models import Company
from django.core.exceptions import ObjectDoesNotExist


def create_complaint_service(company, complaint_type, custom_text=''):
    # Bitta kompaniya, bir QR token — faqat bitta murojaat qilishi uchun check qo‘shish mumkin
    # (masalan, agar frontendda token bo‘lsa yoki complaintni bazadan company va token bo‘yicha qidirish)
    complaint = Complaint.objects.create(
        company=company,
        complaint_type=complaint_type,
        custom_text=custom_text
    )
    return complaint


def get_complaint_list_service(company=None):
    # Adminlar uchun barcha, yoki faqat kompaniya bo‘yicha murojaatlarni olish mumkin
    if company:
        return Complaint.objects.filter(company=company).order_by('-created_at')
    return Complaint.objects.all().order_by('-created_at')


def get_complaint_by_id_service(complaint_id):
    try:
        return Complaint.objects.get(id=complaint_id)
    except ObjectDoesNotExist:
        return None


def mark_complaint_viewed_service(complaint):
    complaint.is_viewed = True
    complaint.save()
    return complaint


def mark_complaint_resolved_service(complaint):
    complaint.is_resolved = True
    complaint.save()
    return complaint


def delete_complaint_service(complaint_id):
    try:
        complaint = Complaint.objects.get(id=complaint_id)
        complaint.delete()
        return True
    except ObjectDoesNotExist:
        return False
