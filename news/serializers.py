from rest_framework import serializers

from news.models import Novelty


class NoveltySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Novelty
        fields = [
            'title',
            'text',
            'created_at',
            'image_url'
        ]
