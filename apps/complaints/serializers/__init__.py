from .List_serializers import ComplaintListSerializer
from .Detail_serializers import ComplaintDetailSerializer
from .Create_serializers import ComplaintCreateSerializer

all = [
    ComplaintListSerializer, ComplaintDetailSerializer, ComplaintCreateSerializer,
]
