from django.shortcuts import render
from rest_framework import generics
from .models import Phones
from .serialzers import PhoneSerializer


class PhoneAPIView(generics.ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhoneSerializer
