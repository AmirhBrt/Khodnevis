from django.db.models import Avg
from rest_framework import serializers

from utils.redis import default_redis, default_pipeline
from contents.models import Content, Rating


class ContentSerializer(serializers.ModelSerializer):
    average_score = serializers.SerializerMethodField()
    ratings_count = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()

    class Meta:
        model = Content
        fields = ['title', 'description', 'author', 'average_score', 'ratings']

    def get_ratings_count(self, obj):
        if ratings_count := default_redis.get(f'contents:ratings_count:{obj.pk}'):
            return int(ratings_count.decode())
        ratings_count = Rating.objects.filter(content=obj).count()
        default_pipeline.set(f'contents:ratings_count:{obj.pk}', ratings_count)
        default_pipeline.execute()
        return ratings_count

    def get_average_score(self, obj):
        if average_score := default_redis.get(f'contents:average_score:{obj.pk}'):
            return float(average_score.decode())
        average_score = Rating.objects.filter(content=obj).aggregate(avg=Avg('score'))['avg'] or 0
        default_pipeline.set(f'contents:average_score:{obj.pk}', str(average_score))
        default_pipeline.execute()
        return average_score

    def get_ratings(self, obj):
        ratings = Rating.objects.filter(content=obj)
        return RatingSerializer(ratings, many=True).data


class ContentListSerializer(ContentSerializer):
    class Meta:
        model = Content
        fields = ['id', 'title', 'author', 'average_score', ]


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['content', 'rater', 'score']
