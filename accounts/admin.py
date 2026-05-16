from django.contrib import admin
from django.contrib import admin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):

    list_display = (
        'user',
        'role',
        'course',
        'phone'
    )

    search_fields = (
        'user__username',
        'role',
        'course'
    )

    list_filter = (
        'role',
        'course'
    )
# Register your models here.
