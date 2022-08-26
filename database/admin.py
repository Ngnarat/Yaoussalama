from django.contrib import admin
from django import forms
from database.models import Regime,  LientFamilial
from compte.models import Payement,User

# Register your models here.

class PaiementForm(forms.ModelForm):
    class Meta:
        model = Payement
        exclude =("utilisateur",)
    
class PaymentAdmin(admin.ModelAdmin):
    fields = ('membre', 'montant','commentaire','utilisateur')
    list_display = ('date', 'membre','montant','utilisateur')
    list_display_links = ('membre','utilisateur')
    list_filter =('membre', 'date', 'utilisateur')
    search_field =('membre')
    readonly_fields = ('utilisateur',)
    form = PaiementForm
    
    def save_model(self, request, obj, form, change):
        obj.utilisateur = str(request.user) + " (" + request.user.username + ")"
        super().save_model(request, obj, form, change)
        
        user = User.objects.get(pk=obj.membre.id) 
        if user.dateLastPayment :
            if user.dateLastPayment < obj.date:
                user.dateLastPayment = obj.date
        else :
            user.dateLastPayment = obj.date        
        user.sumLastPayment = obj.montant
        user.restToPay -= obj.montant
        if user.restToPay > 0:
            user.action = user.RELANCER    
        user.save()



        
        
admin.site.register(Payement,PaymentAdmin)  
admin.site.register(Regime)
admin.site.register(LientFamilial)