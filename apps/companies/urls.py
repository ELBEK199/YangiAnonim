from django.urls import path
from apps.companies.views import CompanyDetailView, CompanyListView, CompanyUpdateView, CompanyCreateView, \
    CompanyDeleteView

urlpatterns = [
    path('', CompanyListView.as_view(), name='company-list'),
    path('Create/', CompanyCreateView.as_view(), name='company-Create'),
    path('<int:company_id>/', CompanyDetailView.as_view(), name='company-detail'),
    path('<int:company_id>/update/', CompanyUpdateView.as_view(), name='company-update'),
    path('<int:company_id>/delete/', CompanyDeleteView.as_view(), name='company-delete'),
]
