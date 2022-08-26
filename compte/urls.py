from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.profil, name = 'profil'),
    path('login', views.login_Page, name = 'login'),
    path('logout', views.logout_page, name = 'logout'),
    path('register', views.register, name = 'register'),
    path('beneficiaires/ajouter',views.adBeneficiaire, name = "ajouter_beneficiaire" ),
    re_path(r'beneficiaires/(?P<idBeneficiaire>[0-9]+)/$',views.AfficheBeneficiaire, name='affiche_beneficiaire'),
    re_path(r'beneficiaires/(?P<idBeneficiaire>[0-9]+)/modifier$', views.UpdateBeneficiaire, name='modifier_beneficiaire'),
    re_path(r'beneficiaires/(?P<idBeneficiaire>[0-9]+)/supprimer$',views.deleteBeneficiaire, name ='supprimer_beneficiaire'),
    re_path(r'paiements$',views.paiementList, name = 'list_paiement' ),
    re_path(r'messages$',views.messageList, name = 'list_message' ),
    re_path(r'messages/nouveau$',views.addmessage, name = 'addmessage'),
]