from django.urls import path
from .views import (
    CompanyListCreateView,
    CompanyDetailUpdateDeleteView,
)

urlpatterns = [
    path('', CompanyListCreateView.as_view(), name='company-list-create'),  # GET (list), POST (create)
    path('<int:company_id>/', CompanyDetailUpdateDeleteView.as_view(), name='company-detail-update-delete'),  # GET, PUT, DELETE
]
