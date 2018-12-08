from django.contrib import admin
from .models import *

class AuthorAdmin(admin.ModelAdmin):
    fields='_all_'


admin.site.register(Location)
admin.site.register(Team)
admin.site.register(Profile)
admin.site.register(User_team)
admin.site.register(Local)
admin.site.register(Space)
admin.site.register(Coworking)
admin.site.register(Status)