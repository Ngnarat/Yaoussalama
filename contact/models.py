from django.db import models
from compte.models import User
from django.core.validators import RegexValidator
# Create your models here.

class Poste(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField(max_length=500)
    
    def __str__(self) -> str:
        return self.nom
    
class Contact(models.Model):
    nom = models.CharField(max_length=150)
    prenom= models.CharField(max_length=150)
    poste = models.ForeignKey(Poste, on_delete=models.SET_NULL, blank=True, null=True)
    phoneNumberRegex = RegexValidator(regex = r"^0[1-9]\d{8}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 11)
    mail = models.EmailField()
    photo = models.ImageField(upload_to ="contact/image", blank = True)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.nom + " " + self.prenom