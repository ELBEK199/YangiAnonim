from django.urls import path
from .views import (
    ComplaintCreateView,
    ComplaintListView,
    ComplaintDetailView,
    ComplaintTypesView
)

urlpatterns = [
    # Oddiy foydalanuvchi murojaat yuboradi (login talab qilinmaydi)
    path('create/', ComplaintCreateView.as_view(), name='complaint-create'),

    # Admin uchun barcha murojaatlar
    path('', ComplaintListView.as_view(), name='complaint-list'),
    path('<int:complaint_id>/', ComplaintDetailView.as_view(), name='complaint-detail'),
    path('types/', ComplaintTypesView.as_view(), name='complaint-types'),
]
