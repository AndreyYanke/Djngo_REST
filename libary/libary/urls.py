"""libary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userapp.views import UserMainModelView
from todoapp.views import ProjectMainModelViewSet, TodoMainModelViewSet
from rest_framework.authtoken import views

router = DefaultRouter()
router.register('user', UserMainModelView)
router.register('project', ProjectMainModelViewSet)
router.register('todo', TodoMainModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-user/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-token-user/', views.obtain_auth_token),
    path('api/users/1.0/', include('userapp.urls', namespace='1.0')),
    path('api/users/2.0/', include('userapp.urls', namespace='2.0')),

]
