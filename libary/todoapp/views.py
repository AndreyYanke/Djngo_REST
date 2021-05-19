from rest_framework.viewsets import ModelViewSet

from .models import ProjectModelSet, TodoModelSet
from .serializers import ProjectMainModelSerializer, TodoMainModelSerializer


class ProjectMainModelViewSet(ModelViewSet):
    queryset = ProjectModelSet.objects.all()
    serializer_class = ProjectMainModelSerializer


class TodoMainModelViewSet(ModelViewSet):
    queryset = TodoModelSet.objects.all()
    serializer_class = TodoMainModelSerializer