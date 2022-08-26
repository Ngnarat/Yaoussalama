from django import forms
from .models import BlogPost
from django import forms

class BlogPostForm(forms.ModelForm):
    
    class Meta:
        model = BlogPost
        fields = ["photo", "title","content","published",]