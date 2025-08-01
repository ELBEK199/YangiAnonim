from .List_view import CompanyListView
from .Detail_view import CompanyDetailView
from .Update_view import CompanyUpdateView
from .Create_view import CompanyCreateView
from .Delete_view import CompanyDeleteView

all = [
    CompanyListView, CompanyDetailView, CompanyUpdateView, CompanyCreateView, CompanyDeleteView
]
