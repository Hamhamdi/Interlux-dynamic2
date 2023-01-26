from datetime import datetime
from email.policy import default
from pyexpat import model
from sqlite3 import Cursor
from unittest.util import _MAX_LENGTH
from django import forms
from tkinter import Widget
from django.db import  models

from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.

user_roles = (
    ('responsable informatique','Responsable Informatique'),
    ('chargee affaire','Chargee Affaire'),
    ('responsable logistique1','Responsable Logistique 1'),
    ('responsable financier','Responsable Financier'),
    ('responsable logistique2','Responsable Logistique 2'),
    )
champ_type = (
    ('VARCHAR','Text'),
    ('DATE','Date'),
    ('BIGINT','number'),
    )
user_etape = (

    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5'),

)
STATUT_IMP = (
    ('',''),
    ('En Negociation','En Négociation'),
    ('Confirmée fournée', 'Confirmée Fournée'),
    ('ex_c_payement','Ex_C_Payement'),
    ('En Préparation','En Préparation'),
    ('Prélevée','Prélevée'),
    ('Arrivée Maroc','Arrivée Maroc'),
    ('En Dédouanement','En Dédouanement'),
    ('Liquidée','Liquidée'),
    ('En Entrepôt','En Entrepôt'),
    ('Livrée','Livrée'),
    ('clôturée','clôturée'),

)


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, etape, role, password=None):
        if not email:
            raise ValueError("users must have an email address")
        if not username:
            raise ValueError("users must have a username")
        if not role:
            raise ValueError("users must have a role")
        if not etape:
            raise ValueError("users must have an etape")

        user = self.model(
            email= self.normalize_email(email),
            username = username,
            role = role,
            etape = etape,
        )
        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self,email, username, etape, role, password=None):

        user = self.create_user(
               email,
               username = username,
               password = password,
               role = role,
               etape = etape,
            )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using = self._db)
        return user

class Base(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique= True)
    # role =  models.ForeignKey(Roles, on_delete=models.CASCADE, null=True)
    role = models.CharField(max_length=100, choices= user_roles, null=True)
    # here we will add an etap for every user
    etape = models.IntegerField(choices= user_etape, null=True)

    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [ 'email','role' , 'etape']

    objects = MyAccountManager()


    def __str__(self):
        return self.username

    def has_perm(self, perm, obj = None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
# here we will add a table for giving any role an etape 


#  here we will add a general table that generate all models from the other users
class GeneralDTable(models.Model):
    # Responsable chargee d'affaire infos:
    n_Dossier = models.IntegerField(null=True)   
    fournisseur = models.CharField(max_length=200,null=True)
    pays = models.CharField(max_length=100, null=True)
    nom = models.CharField(max_length=200,null=True)
    client = models.CharField(max_length=200,null=True)
    date_VCL = models.DateTimeField(null=True)
    date_validation_e1 = models.DateTimeField(null=True)

    # # Responsable Logistique 1 infos:
    statut_Imp = models.CharField(max_length=20, choices=STATUT_IMP, default='',null=True)
    date_TCS = models.DateTimeField(null=True) #date Transmission Commande Service 
    code_Four_Sage = models.CharField(max_length=200, null=True,default='')
    ref_Bon_Cmd_Sage= models.CharField(max_length=200,null=True,default='')
    cat_Cmd = models.CharField(max_length=200,null=True,default='')
    date_CCF = models.DateTimeField(null=True) #date confirmation de la commande fournisseur
    n_FP= models.CharField(max_length=200,null=True,default='')
    date_FP = models.DateTimeField(null=True)
    pays_Origine= models.CharField(max_length=200,null=True,default='')
    incoterm = models.CharField(max_length=200,null=True,default='')
    pays_Prt =models.CharField(max_length=200,null=True,default='')
    montant_Dev = models.CharField(max_length=200, null=True,default='')
    devise=models.CharField(max_length=200,null=True,default='')
    mode_Pay = models.CharField(max_length=200,null=True,default='')
    delai_Liv = models.CharField(max_length=200,null=True,default='')
    Exec_Co_Pay = models.CharField(max_length=200,null=True,default='')
    date_PPF = models.DateTimeField(null=True) #date prevue pickup fournisseur
    date_PAM = models.DateTimeField(null=True) #date prevue arivee au maroc
    date_validation_e2 = models.DateTimeField(null=True)
    delai_e2 = models.IntegerField(null=True)

    # # Responsable Logistique 2 infos:
    date_pickup = models.DateTimeField(null=True) 
    freightforward = models.CharField(max_length=100,null=True,default='')
    mode_trans =  models.CharField(max_length=100,null=True,default='')
    date_AM =  models.CharField(max_length=100,null=True,default='')
    transitaire =  models.CharField(max_length=100,null=True,default='')
    Mt_ded_dh =  models.CharField(max_length=100,null=True,default='')
    date_ld =  models.DateTimeField(null=True)
    date_lc =  models.DateTimeField(null=True)
    litige =  models.CharField(max_length=100,null=True,default='')
    class_litige =  models.CharField(max_length=100,null=True,default='')
    date_validation_e3 = models.DateTimeField(null=True)
    delai_e3 = models.IntegerField(null=True)

    # # Responsable Financier infos:
    date_capf = models.DateTimeField(null=True)
    date_capp = models.DateTimeField(null=True)
    date_validation_e4 = models.DateTimeField(null=True)
    delai_e4 = models.IntegerField(null=True)

    # # Responsable Informatique infos:
    date_cacrs = models.DateTimeField(null=True)
    date_validation_e5 = models.DateTimeField(null=True)
    delai_e5 = models.IntegerField(null=True)

    # statut de dossier 
    etape = models.IntegerField(default = 1)

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

  


    class Meta:
        ordering = ['etape']

  
    def __str__(self):
       return "general table"


# here we have the configuration table for dynamic part
# class ConTable(models.Model):
#     champ = models.CharField(max_length=100,null=True,default='')
#     etape = models.CharField(max_length=100, null=True)
#     column = models.IntegerField(default=1)
#     type = models.CharField(max_length=100, choices= champ_type, null=True)

#     def __str__(self):
#        return "table configuaration"



class Etapes(models.Model):
    name = models.CharField(max_length=100, null=True)
    numero = models.IntegerField(null=True)  
    date_validation = models.DateField(null=True)

    def _str_(self):
        return str(self.numero)

# here we have the configuration table for dynamic part
class ConTable(models.Model):
    champ = models.CharField(max_length=100,null=True,default='')
    etape = models.ForeignKey(Etapes, on_delete=models.CASCADE,null=True, blank=True)
    column = models.IntegerField(default=1)
    type = models.CharField(max_length=100, choices= champ_type, null=True)

    def _str_(self):
       return "table de configuaration"




