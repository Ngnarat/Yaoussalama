from datetime import date, datetime
from django.contrib.auth.models import AbstractUser
from django.db import models
from database.models import Regime, LientFamilial
from PIL import Image

# Create your models here.


    
class User(AbstractUser):
    RAS = 'RAS'
    RELANCER = 'Relancer'
    SUSPENDRE = 'Suspendre'
    ACTION = [
        (RAS, 'à jour'),
        (RELANCER, 'à relancer'),
        (SUSPENDRE, 'à suspendre'),
    ]
    username = models.CharField(verbose_name="Matricule", max_length=150,unique=True,)
    first_name = models.CharField(verbose_name="Nom", max_length=150 )
    last_name = models.CharField(verbose_name="Prenom", max_length=150)
    telephone = models.BigIntegerField(verbose_name="Telephone")
    email = models.EmailField(verbose_name="Mail", unique=True, )
    dateOfBirth  = models.DateField(verbose_name="Date de naissance")
    photo  = models.ImageField(upload_to = 'madia/profil/image', blank=True)
    thumbnail =models.ImageField(upload_to = 'madia/profil/thumbnail', blank=True)
    adresse1 = models.CharField(verbose_name="Adresse 1", max_length= 50)
    adresse2 = models.CharField(verbose_name="Adresse 2",blank=True, max_length= 50)
    ville = models.CharField(max_length= 35, verbose_name="Ville")
    codePostal = models.IntegerField(verbose_name="Code postal")
    country = models.CharField(verbose_name="Pays", max_length= 15)
    regime  = models.ForeignKey(Regime, verbose_name="Regime", on_delete=models.DO_NOTHING,blank=True, null =True)
    action = models.CharField(choices=ACTION, default = RELANCER, max_length= 15,verbose_name="Action")
    dateLastPayment = models.DateField(verbose_name=" Date dernier paiement",blank=True, null =True)
    sumLastPayment = models.DecimalField(verbose_name="Somme payé",max_digits=7, decimal_places=2, default= 0)
    restToPay = models.DecimalField(verbose_name="Reste à cotiser", max_digits=7, decimal_places=2, default= 0)
    echeance = models.DateField(verbose_name="Echeance de cotisation",blank=True, null =True)
    isValidate = models.BooleanField(default=False)
    lastVadidated = models.DateField(blank=True, null=True)
     
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','first_name','last_name','telephone', 'dateOfBirth','adresse1', \
        'codePostal', 'ville','country',]
    
    
    original_isValidate_value = None

    def __init__(self, *args, **kwargs):
        super(User, self).__init__(*args, **kwargs)
        self.original_isValidate_value = self.isValidate

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.isValidate != self.original_isValidate_value:
            if self.isValidate == True:
                lastVadidated =datetime.today()       
        super(User, self).save(force_insert, force_update, *args, **kwargs)
        self.original_isValidate_value = self.isValidate
        
        if self.photo:
            img = Image.open(self.photo.path)
            MYSIZE = (150,250)
            img.thumbnail(MYSIZE)
            img.save(self.photo.path)
      
    def __str__(self):
        return self.first_name + " " + self.last_name


class Beneficiaire (models.Model):
    membre = models.ForeignKey(User,verbose_name="Membre", on_delete= models.CASCADE)
    first_name =  models.CharField(verbose_name="Nom", max_length= 150)
    last_name =  models.CharField(verbose_name="Prenom", max_length= 150)
    dateOfBirth = models.DateField(verbose_name="Date de naissance")
    photo  = models.ImageField(verbose_name="Photo",upload_to = 'media/beneficiaire', blank = True)
    thumbnail =models.ImageField(upload_to = 'madia/beneficiair/thumbnail', blank=True)
    LientFamilial = models.ForeignKey(LientFamilial,verbose_name="Lien de famille", on_delete= models.CASCADE)
    date_joined = models.DateTimeField(verbose_name="Crée le",auto_now_add=True)
    lastUpdate = models.DateTimeField(verbose_name="Modifier le",auto_now=True)
    isActive  = models.BooleanField(verbose_name="Active", default=False)
    
    def __str__(self) -> str:
        return self.first_name + " " + self.last_name
    
    
class Payement (models.Model):
    membre = models.ForeignKey(User, on_delete= models.CASCADE)
    montant = models.DecimalField(verbose_name="Montat",max_digits=7, decimal_places=2)
    date = models.DateField(auto_now_add= True)
    commentaire = models.TextField(verbose_name="Commentaire",max_length=500, blank=True)
    utilisateur = models.CharField( max_length= 150,verbose_name="Déclarant")
    
    
    def __str__(self):
        return str( self.montant)
    

class UserHistory(models.Model):
    ACTIVER = "Activer"
    DESACTIVER = "Désactiver"
    ACTION = [
        (ACTIVER, 'Activer'),
        (DESACTIVER, 'Désactiver'),
    ]
    
    date = models.DateTimeField(auto_now_add=True, verbose_name="Crée le")
    membre = models.ForeignKey(User, verbose_name="Menbre",on_delete=models.CASCADE)
    action = models.CharField(choices=ACTION, verbose_name="Action", max_length=50)
    utilisateur  = models.CharField(verbose_name="Enregistrer par",max_length=150)
    
    
    def __str__(self) -> str:
        return str(self.membre) + ' => ' + self.action