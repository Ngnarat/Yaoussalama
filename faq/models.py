from django.db import models
from compte.models import User

# Create your models here.

class FAQ(models.Model):
    titre = models.CharField(max_length=150)
    contenu = models.TextField(max_length=5000,)
    photo = models.ImageField(upload_to = 'media/faq/photo', blank = True)
    audio = models.FileField(upload_to = 'media/faq/audio', blank = True)
    video = models.FileField(upload_to = 'media/faq/video', blank = True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)
    published =models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return self.titre
    
