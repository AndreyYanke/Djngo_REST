from rest_framework.serializers import HyperlinkedModelSerializer
from .models import ProjectModelSet, TodoModelSet

class ProjectMainModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = ProjectModelSet
        fields = '__all__'

class TodoMainModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = TodoModelSet
        fields = '__all__'

