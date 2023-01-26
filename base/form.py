from dataclasses import fields
from pyexpat import model
from tkinter import Widget
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django.shortcuts import redirect

from .models import  Base, ConTable, GeneralDTable, Etapes



class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=60, help_text='Required. Add a valid email address')
    role = forms.Select()
    etape = forms.Select()

    class Meta:
        model = Base
        fields = ("username","email",  "role", "etape",  "password1", "password2")

class AccountAuthenticationForm(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    # username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    # role = forms.Select()
   

    class Meta :
        model = Base
        fields = ('username', 'password')
        labels = {
            'username':'',
            'password':'',
        }
        widgets = {
            'username':forms.TextInput( attrs={'placeholder': 'Username'}),
            'password':forms.PasswordInput( attrs={'type':'password', 'placeholder': 'Password'}),
        }
    def clean(self):
        if self.is_valid():
            username =self.cleaned_data['username']
            password = self.cleaned_data['password']
            if not authenticate(username=username,  password=password):
                raise forms.ValidationError("invalid")

class Rl1Form(forms.ModelForm):
    
    class Meta:
        model = GeneralDTable
        fields = ['statut_Imp', 'date_TCS',
        'code_Four_Sage','ref_Bon_Cmd_Sage','cat_Cmd', 'date_CCF',
        'n_FP', 'date_FP','pays_Origine',
        'incoterm','pays_Prt', 'montant_Dev','devise', 'mode_Pay','delai_Liv',
        'Exec_Co_Pay','date_PPF', 'date_PAM']
        labels = {
            'statut_Imp':'Statut Importation',
            'code_Four_Sage':'Code Fournisseur Sage',
            'ref_Bon_Cmd_Sage':'Reference bon de commande Sage',
            'cat_Cmd':'Catégorie commande',
            'n_FP':'Numero FP',
            'pays_Origine':'Pays Origine',
            'pays_Prt':'Pays Prelevement',
            'montant_Dev':'Montant Devises',
            'devise':'Devise',
            'mode_Pay':'Mode Payement',
            'delai_Liv':'Delai de livraison',
            'Exec_Co_Pay':'Execution condition payment',
            'date_TCS': 'Date transmission de la commande au service logistique',
            'date_CCF': 'Date Confirmation de commande Fournisseur',
            'date_FP': 'Date FP',
            'date_PPF': 'Date Prevu Pickup Fournisseur',
            'date_PAM': 'Date Prevu Arrivee au maroc',
        }
        widgets = {
            'date_TCS': forms.DateInput(attrs={'type':'date', 'class':'form-control mb-4'}),
            'date_CCF': forms.DateInput(attrs={'type':'date', 'class':'form-control mb-4'}),
            'date_FP': forms.DateInput(attrs={'type':'date', 'class':'form-control mb-4'}),
            'date_PPF': forms.DateInput(attrs={'type':'date', 'class':'form-control mb-4'}),
            'date_PAM': forms.DateInput(attrs={'type':'date', 'class':'form-control mb-4'})
            }

class Rl2Form(forms.ModelForm):
    
    class Meta:
        model = GeneralDTable
        fields = ['date_pickup', 'freightforward','mode_trans',
        'date_AM', 'transitaire','Mt_ded_dh',
         'date_ld','date_lc','litige', 'class_litige']

        widgets = {

            'date_pickup':forms.DateInput(attrs={'type':'date', 'class':'form-control mb-4'}),
            'date_AM':forms.DateInput(attrs={'type':'date', 'class':'form-control mb-4'}),
            'date_ld':forms.DateInput(attrs={'type':'date', 'class':'form-control mb-4'}),
            'date_lc':forms.DateInput(attrs={'type':'date', 'class':'form-control mb-4'}),
            
        }
        labels = {
            'mode_trans':'Mode Transport',
            'date_AM':'Date Arrivee Maroc',
            'Mt_ded_dh':'Montant Dedouanement DH',
            'date_ld':'Date livraison Depot',
            'date_lc':'Date livraison client'


        }
      
class ResInf(forms.ModelForm):
        
    class Meta:
        model = GeneralDTable
        fields = ['date_cacrs']
        labels = {
            'date_cacrs': 'Date Clôture Administrative du Cout de Revient Sage',
        }
        widgets = {'date_cacrs': forms.DateInput(attrs={'type':'date', 'class':'form-control mb-4'})}

class ResFin(forms.ModelForm):
    
    class Meta:
        model = GeneralDTable
        fields = ['date_capf', 'date_capp']
        labels = {
            'date_capf': 'Date du clôture administrative du payement fournisseur',
            'date_capp': ' Date du clôture administrative du payement des partenaires',
        }
        widgets = {
            'date_capf': forms.DateInput(attrs={'type':'date'}),
            'date_capp': forms.DateInput(attrs={'type':'date'})
            }
  
class ResCa(forms.ModelForm):
    class Meta:
        model = GeneralDTable
        fields = ['n_Dossier','fournisseur','pays','nom','client','date_VCL']
        labels = {
            'date_VCL': 'Date du validation des conditions Logistiques',
        }
        widgets = {'date_VCL': forms.DateTimeInput(attrs={'type':'date'})}
      
class GeneralDT(forms.ModelForm):
    class Meta:
        model = GeneralDTable
        fields = '__all__'

class AdminForm(forms.ModelForm):

    class Meta:
        model = ConTable
        fields = ("champ", "etape","type")



from base.dynamic_models import BaseAdmintable




class DynForm(forms.ModelForm):  

    def __init__(self, *args,x, **kwargs):
        self.x = x 
        super(DynForm , self).__init__(*args, **kwargs)
       
        for i in x:
            if i.type == 'DATE':
                self.fields[i.champ] = forms.DateField(widget=forms.DateTimeInput(attrs={'type':'date'}))
                # self.fields[i.champ].widgets.attrs('date')
                # self.widgets.update(({"color" : "red"}))
                #  = {i.champ: forms.DateInput(attrs={'type':'date'})}
            elif i.type == 'VARCHAR':
                self.fields[i.champ] = forms.CharField()
            else:
                self.fields[i.champ] = forms.IntegerField()
  
    class Meta:
        model = BaseAdmintable
        fields = []
        widgets = {}
         
 
class EtapeForm(forms.ModelForm):
    class Meta:
        model = Etapes
        fields = '__all__'

            
