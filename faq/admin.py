from django.contrib import admin
from .models import FAQ
from django import forms
# Register your models here.

class FaqForm(forms.ModelForm):
    
    class Meta:
        model = FAQ
        exclude =('author','created_on','update_on',)

class FaqAdmin(admin.ModelAdmin):
    form = FaqForm
    list_display = ('created_on', 'titre','author','published')
    list_display_links = ('titre',)
    list_filter =('author', 'created_on', 'published')
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
        

admin.site.register(FAQ,FaqAdmin)