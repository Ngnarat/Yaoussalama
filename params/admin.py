from django.contrib import admin
from .models import Param
# Register your models here.


class ParamAdmin(admin.ModelAdmin):
    fields = ('key', 'value','description',)
    list_display = ('key', 'value','description','create_at','update_at')
    list_display_links = ('key',)
    list_filter =('key',)
    readonly_fields = ('create_at','update_at',)
    
admin.site.register(Param,ParamAdmin)    