from rest_framework import serializers

from news.models import Novelty


class UserSerializer(serializers.Serializer):
    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class NoveltySerializer(serializers.HyperlinkedModelSerializer):
    creator = UserSerializer(required=False)

    class Meta:
        model = Novelty
        fields = [
            'title',
            'text',
            'creator',
            'created_at',
            'image_url'
        ]
