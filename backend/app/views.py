from django.shortcuts import render
from .serializers import *
from rest_framework import generics
from .models import DemoUser, Poster

# Create your views here.


class IndexView(generics.ListCreateAPIView):
    queryset = DemoUser.objects.all()
    serializer_class = DemoUserSerializer


class PosterView(generics.ListCreateAPIView):
    queryset = Poster.objects.all()
    serializer_class = PosterSerializer
