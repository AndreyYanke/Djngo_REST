from rest_framework.serializers import HyperlinkedModelSerializer
from .models import UserModelSet

class UserMainModelSerializerV1(HyperlinkedModelSerializer):
    class Meta:
        model = UserModelSet
        fields = ('username', 'first_name', 'last_name', 'email')


class UserMainModelSerializerV2(HyperlinkedModelSerializer):
    class Meta:
        model = UserModelSet
        fields = ('username', 'first_name', 'last_name', 'email','is_staff','is_superuser')
