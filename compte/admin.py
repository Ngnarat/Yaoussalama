from django.contrib import admin
from .models import User, Beneficiaire,UserHistory
import datetime
from params.models import Param
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name','last_name','regime','action',)
    list_display_links = ('username','first_name',)
    list_filter =('first_name', 'last_name', 'regime')
    readonly_fields = ('username','dateLastPayment')
    search_field =("first_name",'last_name')
    
    fieldsets = (
        ('Identité', {
            "fields": ('username', 'first_name','last_name','dateOfBirth' ),
        }),
        ('information',{
            "fields":('email','telephone','regime',"action"),
            }
        ),
        ('Adresse',{
            "fields":('adresse1','adresse2','codePostal','country'),
            }
        ),
        ('Cotisation',{
            "fields":('echeance','dateLastPayment','sumLastPayment','restToPay'),
            }
        ),
         ('Admistration',{
            "fields":('is_active','is_staff','isValidate'),
            }
        ),
    )
    
    def save_model(self, request, obj, form, change):
        if change:
            if obj.isValidate != obj.original_isValidate_value:
                userHistory= UserHistory(membre = obj)
                userHistory.action = UserHistory.ACTIVER if obj.isValidate else UserHistory.DESACTIVER
                userHistory.utilisateur = str(request.user) + " (" + request.user.username + ")"
                userHistory.save()
        else:
            compteur = Param.objects.get(key = "compteur")
            mydate = datetime.datetime.today()
            matricule = mydate.strftime("%m") + mydate.strftime("%Y")[-3:] + "-" + compteur.value
            obj.username = matricule
            compteur.value= str(int(compteur.value)+1)
            compteur.save()
            
        super().save_model(request, obj, form, change)
        
    
        
    
class UserHistoryAdmin(admin.ModelAdmin):
    list_display = ('date', 'membre','action','utilisateur')
    list_filter =('date', 'membre','action','utilisateur')
    def save_model(self, request, obj, form, change):
        obj.utilisateur = str(request.user) + " (" + request.user.username + ")"
        super().save_model(request, obj, form, change)
        
        
admin.site.register(User,UserAdmin)
admin.site.register(Beneficiaire)
admin.site.register(UserHistory,UserHistoryAdmin)

