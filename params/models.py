from django.db import models

# Create your models here.

class Param(models.Model):
    key = models.CharField(verbose_name="Clé", unique=True, max_length=15)
    value = models.CharField(verbose_name="Valeur", max_length=25)
    description = models.TextField(verbose_name="déscription", max_length=500)
    create_at= models.DateField(verbose_name="Crée le",auto_now_add=True)
    update_at = models.DateField(verbose_name="Modifier le", auto_now=True)


    def __str__(self) :
        return self.key