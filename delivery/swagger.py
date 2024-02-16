from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Food Delivery API",
        default_version="v1",
        description="An API for managing food delivery costs ",
        # terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="bsairaghava@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
