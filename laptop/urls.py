from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('laptops/', views.laptop_list, name='laptop_list'),
    path('booking/<int:laptop_id>/', views.booking, name='booking'),
]
