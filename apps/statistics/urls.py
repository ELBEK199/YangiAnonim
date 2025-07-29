from django.urls import path
from apps.statistics.views import (
    StatsByTypeView,
    StatsByCompanyView,
    ComplaintsFilteredView,
)

urlpatterns = [
    path('by-type/', StatsByTypeView.as_view(), name='stats-by-type'),
    path('by-company/', StatsByCompanyView.as_view(), name='stats-by-company'),
    path('complaints/', ComplaintsFilteredView.as_view(), name='stats-complaints-filtered'),
]
