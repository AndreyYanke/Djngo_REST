from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import UserModelSet
from .serializers import UserMainModelSerializer



class UserMainModelView(ListModelMixin,RetrieveModelMixin,CreateAPIView,GenericViewSet):
    queryset = UserModelSet.objects.all()
    serializer_class = UserMainModelSerializer







