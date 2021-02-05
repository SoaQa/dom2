# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from news.models import Novelty
from news.serializers import NoveltySerializer


class NewsViewSet(viewsets.ModelViewSet):
    serializer_class = NoveltySerializer
    lookup_field = 'title'

    def get_queryset(self):
        return Novelty.objects.all()

    def list(self, request, *args, **kwargs):
        if qs := request.GET:
            return Response([NoveltySerializer(i).data for i in Novelty.objects
                .filter(title__icontains=qs.get('title'))])
        else:
            return super().list(request, *args, **kwargs)
