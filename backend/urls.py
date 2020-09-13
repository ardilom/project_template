"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
"""

# django
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# rest framework
from rest_framework import routers

# jwt
from rest_framework import permissions

# views
from .api import views
from .api import viewsets

# drf yasg
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Template",
        default_version='v1',
        description="Template",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register(r'users/admin', viewsets.UserAdminViewSet,
                basename='user_admin')
router.register(r'users/', viewsets.UserViewSet, basename='user')

urlpatterns = [
    path('', views.index_view, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    # swagger
    path('swagger/', schema_view.with_ui(
        'swagger',
        cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui(
        'redoc',
        cache_timeout=0), name='schema-redoc'),
    # api
    path('api/activate/<str:uidb64>/<str:token>/',
         views.activate, name='activate'),
    path('api/authenticate/password/',
         views.authenticate_password, name='login'),
    path('api/get_my_notifications/', views.get_my_notifications),
    path('api/', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
