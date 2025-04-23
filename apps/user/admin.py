from django.contrib import admin
from apps.user.models import PFTUser, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ["user", "id"]


admin.site.register(PFTUser)
admin.site.register(UserProfile, UserProfileAdmin)
