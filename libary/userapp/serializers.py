from rest_framework.serializers import HyperlinkedModelSerializer
from .models import UserModelSet

class UserMainModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = UserModelSet
        fields = ('username', 'first_name', 'last_name', 'email')
