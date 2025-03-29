from django.urls import path
from .views import resource_list, resource_detail, resource_create

urlpatterns = [
    path('', resource_list, name='resource_list'),
    path('create/', resource_create, name='resource_create'),
    path('<int:pk>/', resource_detail, name='resource_detail'),
]
