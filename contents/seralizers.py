from django.db.models import Avg
from rest_framework import serializers

from contents.models import Content, Rating


class ContentSerializer(serializers.ModelSerializer):
    average_score = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = ['title', 'description', 'author', 'average_score', 'ratings']

    def get_average_score(self, obj):
        average_score = Rating.objects.filter(content=obj).aggregate(avg=Avg('score'))['avg'] or 0
        return average_score

    def get_ratings(self, obj):
        ratings = Rating.objects.filter(content=obj)
        return RatingSerializer(ratings, many=True).data

class ContentListSerializer(ContentSerializer):

    class Meta:
        model = Content
        fields = ['id', 'title', 'author', 'average_score',]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['content', 'rater', 'score']
