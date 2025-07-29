from django.db import models
import uuid
from datetime import timedelta, date


def default_expiry():
    return date.today() + timedelta(days=365)


class Company(models.Model):
    name = models.CharField(max_length=255, unique=True)
    identifier = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)  # QR code uchun token
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    qr_expiry = models.DateField(default=default_expiry)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    @property
    def is_qr_valid(self):
        return self.qr_expiry >= date.today()
