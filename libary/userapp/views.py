from rest_framework.viewsets import ModelViewSet

from .models import UserModelSet
from .serializers import UserMainModelSerializer


class UserMainModelView(ModelViewSet):
    queryset = UserModelSet.objects.all()
    serializer_class = UserMainModelSerializer
