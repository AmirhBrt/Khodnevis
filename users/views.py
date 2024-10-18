from rest_framework import viewsets
from rest_framework import permissions

from users.models import User
from users.seralizers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny, )
