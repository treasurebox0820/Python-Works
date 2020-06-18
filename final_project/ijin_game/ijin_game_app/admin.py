from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Member
from .models import Belong, Playing, FaceURL


class CustomUserAdmin(UserAdmin):
    model = Member
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': ('nickname', 'birthdate', )
        }),
    )

    list_display = ['username', 'password', 'nickname',
                    'email', 'birthdate', 'last_login', 'date_joined']


admin.site.register(Member, CustomUserAdmin)
admin.site.register(Belong)
admin.site.register(Playing)
admin.site.register(FaceURL)
