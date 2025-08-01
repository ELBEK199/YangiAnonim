from .List_serializers import CompanyListSerializer
from .Detail_serializers import CompanyDetailSerializer
from .Update_serializers import CompanyUpdateSerializer
from .Create_serializers import CompanyCreateSerializer

all = [
    CompanyUpdateSerializer, CompanyDetailSerializer, CompanyUpdateSerializer, CompanyCreateSerializer,
]
