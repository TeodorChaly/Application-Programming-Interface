from rest_framework import serializers

from .models import Phones


class PhoneSerializer(serializers.ModelSerializer):
    class Mera:
        model = Phones
        fields = ('title')
