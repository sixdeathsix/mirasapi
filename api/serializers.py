from rest_framework import serializers

from .models import *


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    city = serializers.CharField()

    class Meta:
        model = Users
        fields = '__all__'

