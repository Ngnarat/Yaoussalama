from django.contrib import admin
from django import forms
from .models import Message

# Register your models here.
class MessageForm(forms.ModelForm):
    class Meta:
        model =Message
        exclude =('create_at','isRed')
    

class MessageAdmin(admin.ModelAdmin):
    form =MessageForm
    list_display = ('create_at', 'user','sujet','isRed')
    list_display_links = ('sujet',)
    list_filter =('user', 'isRed', 'create_at')


admin.site.register(Message,MessageAdmin)