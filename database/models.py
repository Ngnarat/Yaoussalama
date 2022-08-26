from django.db import models


# Create your models here.

class Regime(models.Model):
    name = models.CharField(verbose_name="Nom", max_length= 15)
    description = models.TextField(verbose_name="Déscription", max_length= 300)
    montant = models.IntegerField(verbose_name="Montant")
    
    def __str__(self):
        return self.name



class LientFamilial(models.Model):
    name = models.CharField(verbose_name="Nom", max_length= 15)
    description = models.CharField(verbose_name="Déscription", max_length= 15)
    
    def __str__(self):
        return self.name

