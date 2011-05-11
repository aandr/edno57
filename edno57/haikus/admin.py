from django.contrib import admin
from haikus.models import Haiku

class HaikuAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('user', 'text', 'created')


admin.site.register(Haiku, HaikuAdmin)
