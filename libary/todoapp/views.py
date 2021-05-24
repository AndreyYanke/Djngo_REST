from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .models import ProjectModelSet, TodoModelSet
from .serializers import ProjectMainModelSerializer, TodoMainModelSerializer


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 20


class ProjectMainModelView(ModelViewSet):
    queryset = ProjectModelSet.objects.all()
    serializer_class = ProjectMainModelSerializer
    pagination_class = ProjectLimitOffsetPagination
    filterset_fields = ['name']


class TodoMainModelView(ModelViewSet):
    queryset = TodoModelSet.objects.all()
    serializer_class = TodoMainModelSerializer
    pagination_class = TodoLimitOffsetPagination
    filterset_fields = ['project']
    search_fields = ['username', 'email']

    def destroy(self, request, *args, **kwargs):
        todo = TodoModelSet.objects.get(id=int(kwargs.get('pk')))
        todo.active = False
        todo.save()
        serializer = TodoMainModelSerializer(todo)
        return Response(serializer.data)


