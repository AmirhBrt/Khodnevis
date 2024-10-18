from rest_framework import viewsets, permissions

from contents.models import Content, Rating
from contents.seralizers import ContentSerializer, ContentListSerializer, RatingSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        if self.action == 'list':
            return ContentListSerializer
        return ContentSerializer


class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    permission_classes = [permissions.AllowAny]
