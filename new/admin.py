from django.contrib import admin


from django.contrib import admin
from new.models import *

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, AuthorAdmin)
# Register your models here.

class GroupAdmin(admin.ModelAdmin):
    list_display = ['groupname',]
admin.site.register(Group, GroupAdmin)


class PermiAdmin(admin.ModelAdmin):
    list_display = ['permision','description']
admin.site.register(Permission, PermiAdmin)
