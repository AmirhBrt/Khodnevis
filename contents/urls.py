from django.urls import path

from contents.views import ContentViewSet, RatingViewSet

urlpatterns = [
    path('', ContentViewSet.as_view({'get': 'list', 'post': 'create'}), name='contents'),
    path('<int:pk>/', ContentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='contents_detail'),
    path('rate/', RatingViewSet.as_view({'get': 'list', 'post': 'create'}), name='rate'),
]
