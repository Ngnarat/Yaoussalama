from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('about', views.about, name = 'about'),
    path('blog', views.blog, name = 'blog'),
    path('concact', views.contact, name = 'contact'),
    path('faq', views.faq, name = 'faq'),
]