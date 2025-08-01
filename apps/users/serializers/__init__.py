from .List_serializers import UserListSerializer
from .Detail_serializers import UserDetailSerializer
from .Create_serializers import UserCreateSerializer

all = [
    UserListSerializer, UserDetailSerializer, UserCreateSerializer,
]
