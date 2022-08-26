from django.db import models
from compte.models import User

# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(User, verbose_name="Membre", on_delete=models.CASCADE)
    sujet = models.CharField(max_length=150, verbose_name="Sujet")
    message = models.TextField(max_length=5000, verbose_name="Message")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Date")
    isRed = models.BooleanField(default=False,verbose_name="Lu")
    
    
    class Meta:
        ordering = ['-create_at']
        verbose_name = "Message"
        
    def __str__(self) -> str:
        return self.sujet