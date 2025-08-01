from .List_view import UserListView
from .Detail_view import UserDetailView
from .Update_view import UserUpdateView
from .Create_view import UserCreateView
from .Delete_view import UserDeleteView

all = [
    UserListView, UserDetailView, UserUpdateView, UserCreateView, UserDeleteView,
]
