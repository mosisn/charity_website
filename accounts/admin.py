from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    list_filter = ('gender', 'is_staff', 'is_active', 'is_superuser')
    list_editable = ('is_staff', 'is_active')
    search_fields = ('username', 'email', 'phone')

    fieldsets = (
        (None, {
            'fields' : ('username', 'password'),
            'classes' : ('wide',)
        }),
        ('Personal info',{
            'fields' : ('first_name','last_name', 'email', 'gender', 'age', 'description'),
            'classes' : ('wide',)
        }),
        ('Contact info',{
            'fields' : ('phone', 'address'),
            'classes' : ('wide',)
        }),
        ('Permissions',{
            'fields' : ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
            'classes' : ('wide',)
        }),
        ('Important dates',{
            'fields' : ('last_login', 'date_joined')
        })
    )

admin.site.register(User, UserAdmin)