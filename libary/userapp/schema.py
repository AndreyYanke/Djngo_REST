# import graphene
# from graphene_django import DjangoObjectType
# from userapp.models import UserModelSet
#
#
# class UserType(DjangoObjectType):
#     class Meta:
#         model = UserModelSet
#         fields = '__all__'
#
#
# class Query(graphene.ObjectType):
#     all_users = graphene.List(UserType)
#
#     def resolve_all_users(self, info):
#         return UserModelSet.objects.all()
#
#
# schema = graphene.Schema(query=Query)
