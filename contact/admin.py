from django.contrib import admin
from .models import Contact, Poste
from django import  forms

# Register your models here.

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        exclude =('author','created_on','update_on',)

class ContactAdmin(admin.ModelAdmin):
    form = ContactForm
    list_display = ('nom','prenom', 'poste')
    list_display_links = ('nom','prenom',)
    # list_filter =('author', 'created_on', )
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
        
admin.site.register(Poste)
admin.site.register(Contact,ContactAdmin)