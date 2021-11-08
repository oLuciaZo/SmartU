from django.contrib import admin

# Register your models here.

from .models import Switches, Brand, Participants

class SwitchesAdmin(admin.ModelAdmin):
    list_display=('title','slug')
    list_filter=('title',)
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Switches, SwitchesAdmin)
admin.site.register(Brand)
admin.site.register(Participants)