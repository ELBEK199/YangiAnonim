import uuid
from apps.companies.models import Company
from django.core.exceptions import ObjectDoesNotExist
from django.conf import settings
import qrcode
from io import BytesIO
from django.core.files.base import ContentFile
from datetime import date


def create_company_service(name, qr_expiry=None):
    identifier = uuid.uuid4()
    if qr_expiry is None:
        qr_expiry = date.today().replace(year=date.today().year + 1)
    company = Company.objects.create(
        name=name,
        identifier=identifier,
        qr_expiry=qr_expiry
    )
    generate_and_save_qr_code(company)
    return company


def update_company_service(company, data):
    if 'name' in data:
        company.name = data['name']
    if 'qr_expiry' in data:
        company.qr_expiry = data['qr_expiry']
    company.save()
    generate_and_save_qr_code(company, update=True)
    return company


def delete_company_service(company_id):
    try:
        company = Company.objects.get(id=company_id)
        company.delete()
        return True
    except ObjectDoesNotExist:
        return False


def get_company_by_id_service(company_id):
    try:
        return Company.objects.get(id=company_id)
    except ObjectDoesNotExist:
        return None


def get_company_list_service():
    return Company.objects.all().order_by('-created_at')


def generate_and_save_qr_code(company, update=False):
    # QR da kompaniya identifier/tokeni va expiry’ni kodlaymiz
    qr_content = f"{company.identifier}|{company.qr_expiry.isoformat()}"
    qr_img = qrcode.make(qr_content)
    buffer = BytesIO()
    qr_img.save(buffer, format="PNG")
    filename = f"{company.identifier}.png"
    file_content = ContentFile(buffer.getvalue())
    company.qr_code.save(filename, file_content, save=True if not update else False)
    if update:
        company.save()
