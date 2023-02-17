from django.contrib import admin
from django.urls import path, include

from api.views import *
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'city', CityViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('api/', include(router.urls))
]
