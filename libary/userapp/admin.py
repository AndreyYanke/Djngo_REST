from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModelSet


admin.site.register(UserModelSet, UserAdmin)