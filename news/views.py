from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from news.models import Novelty
from news.serializers import NoveltySerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = Novelty.objects.all()
    serializer_class = NoveltySerializer
