from django.urls import path
from .views import patient_list, patient_detail, patient_create

urlpatterns = [
    path('', patient_list, name='patient_list'),
    path('create/', patient_create, name='patient_create'),
    path('<int:pk>/', patient_detail, name='patient_detail'),
]
