from rest_framework import viewsets

from .serializers import *
from .models import *


class CityViewSet(viewsets.ModelViewSet):
    queryset = Cities.objects.all()
    serializer_class = CitySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UserSerializer
