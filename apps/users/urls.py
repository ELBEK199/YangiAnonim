from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users.views import UserCreateView, UserDetailView, UserUpdateView, UserDeleteView
from apps.users.views.List_view import CustomTokenObtainPairView, UserListView
from apps.users.views.User_me import UserMeView

urlpatterns = [
    # JWT login
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/token/', TokenRefreshView.as_view(), name='token_refresh'),

    # Users CRUD (faqat adminlar uchun)
    path('', UserListView.as_view(), name='user-list'),
    path('me/', UserMeView.as_view(), name='users-me'),

    # Yaratish (POST)
    path('create/', UserCreateView.as_view(), name='user-create'),

    # Detail (GET)
    path('<int:user_id>/', UserDetailView.as_view(), name='user-detail'),

    # Update (PUT)
    path('<int:user_id>/update/', UserUpdateView.as_view(), name='user-update'),

    # Delete (DELETE)
    path('<int:user_id>/delete/', UserDeleteView.as_view(), name='user-delete'),
]
