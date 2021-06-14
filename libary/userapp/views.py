from rest_framework.generics import CreateAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet

from .models import UserModelSet
from .serializers import UserMainModelSerializerV1, UserMainModelSerializerV2



class UserMainModelView(ListModelMixin,RetrieveModelMixin,CreateAPIView,GenericViewSet):
    queryset = UserModelSet.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserMainModelSerializerV2
        return UserMainModelSerializerV1







