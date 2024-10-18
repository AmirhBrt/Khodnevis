from django.urls import path
from rest_framework.authtoken import views as drf_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from users.views import UserViewSet

urlpatterns = [
    path('', UserViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-token-auth/', drf_views.obtain_auth_token, name='api_token_auth'),
]
