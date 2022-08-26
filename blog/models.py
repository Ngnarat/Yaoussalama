from django.db import models
from django.conf import settings

# Create your models here.

class BlogPost(models.Model):
    photo = models.ImageField(upload_to = 'media/blog', null=True, blank=True)
    title = models.CharField(max_length=128)
    content = models.TextField(max_length=5000)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    last_updated = models.DateTimeField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    
       
    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title

