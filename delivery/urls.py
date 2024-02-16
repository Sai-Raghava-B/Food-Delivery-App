from django.urls import path
from . import views
from .swagger import schema_view
urlpatterns = [
    path('calculate_delivery_cost/', views.calculate_delivery_cost, name='calculate_delivery_cost'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('swagger.json', schema_view.without_ui(cache_timeout=0), name='schema-json'),
]
