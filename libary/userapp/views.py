from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import UserModelSet
from .serializers import UserMainModelSerializer



class UserMainModelView(ListModelMixin, CreateModelMixin, RetrieveModelMixin,GenericViewSet):
    queryset = UserModelSet.objects.all()
    serializer_class = UserMainModelSerializer







