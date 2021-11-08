from django.contrib import admin

# Register your models here.
from .models import Capacity
class CapacityAdmin(admin.ModelAdmin):
    list_display=('building','ap','client')
    list_filter=('building',)
    #prepopulated_fields = {'client': ('building',)}

admin.site.register(Capacity,CapacityAdmin)