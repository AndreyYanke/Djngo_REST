from django.urls import path
from .views import UserMainModelView

app_name = 'authors'
urlpatterns = [
    path('', UserMainModelView.as_view({'get': 'list'}))
]