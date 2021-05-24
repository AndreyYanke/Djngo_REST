from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import GenericViewSet

from rest_framework.viewsets import ModelViewSet
from .models import UserModelSet
from .serializers import UserMainModelSerializer

# class UserMainModelView(ModelViewSet):
#     queryset = UserModelSet.objects.all()
#     serializer_class = UserMainModelSerializer
#     filterset_fields = ['id', 'username']


class UserLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3

class UserMainModelView(ListModelMixin, CreateModelMixin, RetrieveModelMixin,GenericViewSet):
    queryset = UserModelSet.objects.all()
    serializer_class = UserMainModelSerializer
    pagination_class =UserLimitOffsetPagination
    filterset_fields = ['id', 'username']





