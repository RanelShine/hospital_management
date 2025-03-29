from django.urls import path
from .views import personnel_list, personnel_detail, personnel_create

urlpatterns = [
    path('', personnel_list, name='personnel_list'),
    path('create/', personnel_create, name='personnel_create'),
    path('<int:pk>/', personnel_detail, name='personnel_detail'),
]
