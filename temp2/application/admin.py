from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class FlatPageAdmin(admin.ModelAdmin):

    fieldsets = [
        *UserAdmin.fieldsets, 
        (
            'Custom Field Heading',
            {
                "fields": ["college"],
            },
        ),
    ]
admin.site.register(CustomUser, FlatPageAdmin)