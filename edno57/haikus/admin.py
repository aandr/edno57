from django.contrib import admin
from haikus.models import Haiku


class HaikuAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    list_display = ('user', 'text', 'created')
    search_fields = ('text', 'user__username')
    save_on_top = True


admin.site.register(Haiku, HaikuAdmin)
