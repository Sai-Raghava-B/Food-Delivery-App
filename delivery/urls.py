from django.urls import path
from . import views

urlpatterns = [
    path('calculate_delivery_cost/', views.calculate_delivery_cost, name='calculate_delivery_cost'),
]
