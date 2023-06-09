from django.shortcuts import render
from rest_framework import generics
from .serializers import ExperienceSerializer
from .models import Experience


def index(request):
    return render(request, 'index.html')


class ExperienceList(generics.ListCreateAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer


class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer
