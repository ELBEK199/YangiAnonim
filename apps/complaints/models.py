from django.db import models
from apps.companies.models import Company

COMPLAINT_CHOICES = [
    ('oshxona', "Oshxonada ovqat me'yorida berilmayapti"),
    ('kiyim', "Kiyim-kechak o'z vaqtida me'yor asosida tarqatilmayapti"),
    ('tamagirlik', "Lavozimga tayinlash va ko'tarishda tamagirlik qilinmoqda"),
    ('zoravonlik', "Komandirlar jismoniy zo'ravonlik bilan shug'ullanmoqda"),
    ('pul_yigish', "Komandirlar turli sabablarga ko'ra pul yig'ayapti"),
    ('tengsizlik', "Rag'batlantirishda ijtimoiy tengsizlikka rioya qilinmayapti"),
    ('pul_tolov', "Menga pul ta'minoti to'liq to'lanmayapti"),
    ('shaxsiy_fikr', "Harbir xizmatchining shaxsiy fikri"),
]

class Complaint(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="complaints")
    complaint_type = models.CharField(max_length=30, choices=COMPLAINT_CHOICES)
    custom_text = models.TextField(blank=True)  # Faqat “shaxsiy_fikr” uchun
    created_at = models.DateTimeField(auto_now_add=True)
    is_viewed = models.BooleanField(default=False)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.company.name} - {self.get_complaint_type_display()} - {self.created_at.date()}"
