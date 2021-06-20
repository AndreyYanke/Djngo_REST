import graphene
from graphene_django import DjangoObjectType
from userapp.models import UserModelSet
from todoapp.models import Project, Todo


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = UserModelSet
        fields = '__all__'


class TodoType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserType)

    def resolve_all_users(root, info):
        return UserModelSet.objects.all()

    all_todos = graphene.List(TodoType)

    def resolve_all_todos(root, info):
        return Todo.objects.all()

    all_projects = graphene.List(ProjectType)

    def resolve_all_projects(root, info):
        return Project.objects.all()


schema = graphene.Schema(query=Query)
