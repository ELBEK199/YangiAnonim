from django.urls import path
from .views import (
    CustomTokenObtainPairView,
    UserListCreateView,
    UserDetailUpdateDeleteView
)

urlpatterns = [
    # JWT login
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),

    # Users CRUD (faqat adminlar uchun)
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:user_id>/', UserDetailUpdateDeleteView.as_view(), name='user-detail-update-delete'),
]
