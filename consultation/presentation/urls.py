from django.urls import path
from .views import consultation_list, consultation_detail, consultation_create

urlpatterns = [
    path('', consultation_list, name='consultation_list'),
    path('create/', consultation_create, name='consultation_create'),
    path('<int:pk>/', consultation_detail, name='consultation_detail'),
]
