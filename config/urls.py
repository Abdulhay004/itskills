from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib.auth.decorators import user_passes_test
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

# schema_view = get_schema_view(
#    openapi.Info(
#       title="My API",
#       default_version='v1',
#       description="Test description",
#       terms_of_service="https://www.google.com/policies/terms/",
#       contact=openapi.Contact(email="contact@myapi.local"),
#       license=openapi.License(name="BSD License"),
#    ),
#    public=True,
#    permission_classes=(permissions.AllowAny,),
# )

def is_superuser(user):
    # return user.is_superuser    # faqat superuserlar ko'ra oladi
    # return user.is_authenticated
    return True
    # return True qilinsa istalgan user kira oladi

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
]


urlpatterns += [
    path('schema/', user_passes_test(is_superuser)(SpectacularAPIView.as_view()), name='schema'),
    path('swagger/', user_passes_test(is_superuser)(SpectacularSwaggerView.as_view()), name='swagger-ui'),
    path('redoc/', user_passes_test(is_superuser)(SpectacularRedocView.as_view()), name='redoc'),
]