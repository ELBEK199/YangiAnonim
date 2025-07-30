from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    CustomTokenObtainPairView,
    UserListCreateView,
    UserDetailUpdateDeleteView
)

urlpatterns = [
    # JWT login
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Users CRUD (faqat adminlar uchun)
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:user_id>/', UserDetailUpdateDeleteView.as_view(), name='user-detail-update-delete'),
]
