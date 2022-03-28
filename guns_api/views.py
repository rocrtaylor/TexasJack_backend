from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializers import GunSerializer
from .models import Gun

class GunList(generics.ListCreateAPIView):
  queryset = Gun.objects.all().order_by('id')
  serializer_class = GunSerializer

class GunDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Gun.objects.all().order_by('id')
  serializer_class = GunSerializer