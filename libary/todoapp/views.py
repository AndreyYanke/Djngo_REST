from rest_framework.viewsets import ModelViewSet

from .models import ProjectModelSet, TodoModelSet
from .serializers import ProjectMainModelSerializer, TodoMainModelSerializer


class ProjectMainModelView(ModelViewSet):
    queryset = ProjectModelSet.objects.all()
    serializer_class = ProjectMainModelSerializer


class TodoMainModelView(ModelViewSet):
    queryset = TodoModelSet.objects.all()
    serializer_class = TodoMainModelSerializer