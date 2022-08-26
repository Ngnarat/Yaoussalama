from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404, render,redirect
from .forms import LoginForm, RegisterForm
from params.models import Param
from compte.models import Beneficiaire, Payement
import datetime
from django.contrib.auth.decorators import login_required
from message.models import Message
from message.forms import MessageForm




# Create your views here.

def login_Page(request):
    if request.user.is_authenticated:
        return redirect('profil')
    else:
        form = LoginForm()
        
        if request.method == 'POST':
            form = LoginForm()(request.POST)
            if form.is_valid():
                user = authenticate(
                    username = form.cleaned_data['mail'],
                    password = form.cleaned_data['password'],
                )
                if user is not None:
                    login(request, user)
                    return redirect('profil')   
                         
        return render(request, 'compte/login.html', context={'form': form})   

@login_required
def logout_page(request):
    logout(request)
    return redirect('home')


def register(request):
    if request.user.is_authenticated:
        return redirect('profil')
    else:
        form = RegisterForm()
        compteur = Param.objects.get(key = "compteur")
        mydate = datetime.datetime.today()
        matricule = mydate.strftime("%m") + mydate.strftime("%Y")[-3:] + compteur.value # + '{:05}'.format(compteur.value)
        if request.method == 'POST':
           # message= "compteur vaut :" + compteur.value
            form = RegisterForm(request.POST)
            if form.is_valid():
                #user = User(form.cleaned_data)
                if compteur:
                    mydate = datetime.datetime.today()
                    #matricule = str(mydate.month) + str(mydate.year)[-3:] + '{:05}'.format(compteur.value)
                    form.instance.username = matricule
                    user = form.save()
                    compteur.value= str(int(compteur.value)+1)
                    compteur.save()
                    login(request, user)
                    return redirect('profil')  
        return render(request, 'compte/register.html', context={'form':form, "message" : matricule})  
  
    
@login_required
def profil(request):
    beneficiaire = Beneficiaire.objects.filter(membre = request.user.id)
    # if Beneficiaire.DoesNotExist:
    #     beneficiaire =[]
    return render(request,"compte/profil.html", context={"user": request.user, "beneficiaire": beneficiaire} )
    


@login_required
def AfficheBeneficiaire(request,idBeneficiaire):
    beneficiaire =  get_object_or_404(Beneficiaire,pk=idBeneficiaire)
    return render(request, "compte/beneficiaires/afficherBeneficiaireForm.html",context={"beneficiaire": beneficiaire})   
            
    
@login_required    
def adBeneficiaire(request):
    form = forms.BeneficaireForm()
    if request.method == "POST":
        form  = forms.BeneficaireForm(request.POST, request.FILES)
        if form.is_valid(): 
            beneficiaire = form.save(commit = False)
            beneficiaire.membre = request.user
            beneficiaire.save()
            return redirect('profil') 
    return render(request, "compte/beneficiaires/createBeneficiaireForm.html",context={"form": form})   
        
            
@login_required
def UpdateBeneficiaire(request, idBeneficiaire):
    beneficiaire =  get_object_or_404(Beneficiaire,pk=idBeneficiaire)
    form =forms.BeneficaireForm(request.POST or None,request.FILES or None, instance = beneficiaire)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('affiche_beneficiaire',idBeneficiaire) 
    return render(request, 'compte/beneficiaires/updateBeneficiaireForm.html', {'form':form}) 

   
@login_required
def deleteBeneficiaire(request, idBeneficiaire):
    beneficiaire =  get_object_or_404(Beneficiaire,pk=idBeneficiaire)
    beneficiaire.delete()
    

@login_required
def paiementList(request):
    paiements = Payement.objects.filter(membre = request.user.id)
    # if Payement.DoesNotExist:
    #     paiements =[]
    return render(request, "compte/paiements/listPaiement.html", context={"paiements":paiements}) 


@login_required
def messageList(request):
    messages = Message.objects.filter(user = request.user.id)
    # if Message.DoesNotExist:
    #     messages =[]
    return render(request, "compte/messages/listMessage.html", context={"messages":messages}) 

@login_required
def addmessage(request):
    form  = MessageForm()
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('list_message')
    
    return render(request, "compte/messages/addMessage.html", context={"form":form})

