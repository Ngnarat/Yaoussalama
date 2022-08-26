from django.contrib import admin
from .models import BlogPost
from .forms import BlogPostForm
# Register your models here.

class BlogPostAdmin(admin.ModelAdmin):
    # fields = ('membre', 'montant','commentaire','utilisateur')
    list_display = ('created_on', 'title','author','published')
    list_display_links = ('title',)
    list_filter =('author', 'created_on', 'published')
    # readonly_fields = ('utilisateur',)
    form = BlogPostForm
    
    def save_model(self, request, obj, form, change):
        obj.author = request.user
        super().save_model(request, obj, form, change)
    


admin.site.register(BlogPost,BlogPostAdmin) 

