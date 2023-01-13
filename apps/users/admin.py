from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.users.models import UserProfile


# 对UserProfile表创建一个管理器
class UserProfileAdmin(admin.ModelAdmin):
    pass


# 将表和管理器关联起来
admin.site.register(UserProfile, UserAdmin)
