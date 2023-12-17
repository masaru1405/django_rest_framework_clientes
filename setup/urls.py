from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from clientes.views import ClienteViewSet

router = routers.DefaultRouter()
router.register('clientes', ClienteViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
