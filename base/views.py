from asyncore import write
from dataclasses import fields
from datetime import date, datetime
import email
from email.mime import base
from lib2to3.pgen2.pgen import generate_grammar
import os
from tracemalloc import start
from typing import OrderedDict
from urllib import response
from django.db import connection
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from itertools import chain
from importlib import import_module,reload
from django.conf import settings
from django.urls import clear_url_caches, is_valid_path
 

from operator import attrgetter
from django.db.models import Q
from django.contrib import admin


import xlwt
from django.http import HttpResponse
import csv


from base.context_processor import get_notified


# from base.dynamic_models import BaseDyngt
from base.form import  AdminForm, DynForm,  RegistrationForm,EtapeForm, AccountAuthenticationForm, ResCa, ResFin, ResInf, Rl1Form, Rl2Form
from django.db.models.functions import Upper

# from base.form import RoleForm
from .models import  Base, ConTable,   GeneralDTable, Etapes
from django.contrib.auth.forms import UserCreationForm
from django.forms import modelformset_factory
from .dynamic_models import BaseAdmintable
from django.forms import DateInput

from django.contrib import admin



# Create your views here.




def loginPage(request):
    context = {}
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    if request.POST:
        form = AccountAuthenticationForm(request.POST)

        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:

                login(request, user)
                return redirect('general_db')

    else:
       form = AccountAuthenticationForm()

    context['login_form'] = form
    return render(request, 'base/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            role = form.cleaned_data.get('role')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, role=role, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:  # GET request
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'base/register.html', context)

def home(request):
    return render(request, 'base/home.html')


def addRCa(request):
    
    form = ResCa()
 
    if request.method == 'POST':
        form = ResCa(request.POST)

        if form.is_valid():
            resca =form.save(commit=False)       
            resca.date_validation_e1 = datetime.now()
            if 'btn_submit' in request.POST:
                 resca.etape+=1
            resca.save()
           


            
            

            return redirect('general_db')
        
    context={'form': form}
    return render(request, 'base/respo_ca_add.html', context)
    
@login_required(login_url='/login')
def updateRCa (request, pk):

    rca = GeneralDTable.objects.get(id=pk)
    form = ResCa(instance=rca)
   

    if request.method == 'POST':
        form = ResCa(request.POST, instance=rca) 
        if form.is_valid():
            resca =form.save(commit=False)  
            resca.date_validation_e1 = datetime.now()
            if 'btn_submit' in request.POST:
                 resca.etape+=1
            resca.save()
            return redirect('general_db')
    context={'form': form}
    return render(request, 'base/respo_ca_add.html', context)


@login_required(login_url='/login')
def updatelog1 (request, pk):
    log1 = GeneralDTable.objects.get(id=pk)
    form = Rl1Form(instance=log1)

    if request.POST:
        form = Rl1Form(request.POST, instance=log1)
        if form.is_valid():
            
            reslog1 =form.save(commit=False)     
            log1.statut_Imp =  reslog1.statut_Imp
            log1.date_TCS =  reslog1.date_TCS
            log1.code_Four_Sage =  reslog1.code_Four_Sage
            log1.ref_Bon_Cmd_Sage =  reslog1.ref_Bon_Cmd_Sage
            log1.cat_Cmd =  reslog1.cat_Cmd
            log1.date_CCF =  reslog1.date_CCF
            log1.n_FP =  reslog1.n_FP
            log1.date_FP =  reslog1.date_FP
            log1.pays_Origine =  reslog1.pays_Origine
            log1.incoterm =  reslog1.incoterm
            log1.pays_Prt =  reslog1.pays_Prt
            log1.montant_Dev =  reslog1.montant_Dev
            log1.devise =  reslog1.devise
            log1.mode_Pay =  reslog1.mode_Pay
            log1.delai_Liv =  reslog1.delai_Liv
            log1.Exec_Co_Pay =  reslog1.Exec_Co_Pay
            log1.date_PPF =  reslog1.date_PPF
            log1.date_PAM =  reslog1.date_PAM
            log1.date_validation_e2 = datetime.now()
          
            delta = log1.date_validation_e2 - log1.date_validation_e1
            log1.delai_e2 = delta.days + 1


            if 'btn_submit' in request.POST:
                log1.etape+=1
            log1.save()
            return redirect('general_db')


    context={'form': form, 'log1':log1}
    return render(request, 'base/respo_log1_add.html', context)           
def addlog1(request, pk):

    form = Rl1Form()
    log1 = GeneralDTable.objects.get(id=pk)
   

    if request.POST:
        form = Rl1Form(request.POST)
        if form.is_valid():
            
            reslog1 =form.save(commit=False)     
            log1.statut_Imp =  reslog1.statut_Imp
            log1.date_TCS =  reslog1.date_TCS
            log1.code_Four_Sage =  reslog1.code_Four_Sage
            log1.ref_Bon_Cmd_Sage =  reslog1.ref_Bon_Cmd_Sage
            log1.cat_Cmd =  reslog1.cat_Cmd
            log1.date_CCF =  reslog1.date_CCF
            log1.n_FP =  reslog1.n_FP
            log1.date_FP =  reslog1.date_FP
            log1.pays_Origine =  reslog1.pays_Origine
            log1.incoterm =  reslog1.incoterm
            log1.pays_Prt =  reslog1.pays_Prt
            log1.montant_Dev =  reslog1.montant_Dev
            log1.devise =  reslog1.devise
            log1.mode_Pay =  reslog1.mode_Pay
            log1.delai_Liv =  reslog1.delai_Liv
            log1.Exec_Co_Pay =  reslog1.Exec_Co_Pay
            log1.date_PPF =  reslog1.date_PPF
            log1.date_PAM =  reslog1.date_PAM
            log1.date_validation_e2 = datetime.now()
            delta = log1.date_validation_e2 - log1.date_validation_e1
            log1.delai_e2 = delta.days + 1
            if 'btn_submit' in request.POST:
                log1.etape+=1
            log1.save()
            
             


            return redirect('general_db')


    context={'form': form, 'log1':log1}
    return render(request, 'base/respo_log1_add.html', context)

@login_required(login_url='/login')
def updatelog2(request, pk):
    log2 = GeneralDTable.objects.get(id=pk)
    form = Rl2Form(instance=log2)
    if request.POST:

        form = Rl2Form(request.POST, instance=log2)
        if form.is_valid():
            reslog2 =form.save(commit=False)     
            
            log2.date_pickup =  reslog2.date_pickup
            log2.freightforward =  reslog2.freightforward
            log2.mode_trans =  reslog2.mode_trans
            log2.date_AM =  reslog2.date_AM
            log2.transitaire =  reslog2.transitaire
            log2.Mt_ded_dh =  reslog2.Mt_ded_dh
            log2.date_ld =  reslog2.date_ld
            log2.date_lc =  reslog2.date_lc
            log2.litige =  reslog2.litige
            log2.class_litige =  reslog2.class_litige           
            log2.date_validation_e3 = datetime.now()
            delta = log2.date_validation_e3 - log2.date_validation_e2
            log2.delai_e3 = delta.days + 1
            if 'btn_submit' in request.POST:
                log2.etape+=1
            log2.save()
            
            

            return redirect('general_db')

    context={'form': form}
    return render(request, 'base/respo_log2_add.html', context)
def addlog2(request, pk):
    
    form = Rl2Form()
    log2 = GeneralDTable.objects.get(id=pk)
    

    if request.POST:
        form = Rl2Form(request.POST)
        if form.is_valid():
            reslog2 =form.save(commit=False)     
            
            log2.date_pickup =  reslog2.date_pickup
            log2.freightforward =  reslog2.freightforward
            log2.mode_trans =  reslog2.mode_trans
            log2.date_AM =  reslog2.date_AM
            log2.transitaire =  reslog2.transitaire
            log2.Mt_ded_dh =  reslog2.Mt_ded_dh
            log2.date_ld =  reslog2.date_ld
            log2.date_lc =  reslog2.date_lc
            log2.litige =  reslog2.litige
            log2.class_litige =  reslog2.class_litige           
            log2.date_validation_e3 = datetime.now()
            delta = log2.date_validation_e3 - log2.date_validation_e2
            log2.delai_e3 = delta.days + 1          
            if 'btn_submit' in request.POST:
                log2.etape+=1
            log2.save()
            
            

            return redirect('general_db')

    context={'form': form}
    return render(request, 'base/respo_log2_add.html', context)

@login_required(login_url='/login')
def updatefin(request, pk):
    

    fin = GeneralDTable.objects.get(id=pk)
    form = ResFin(instance=fin)

   

    if request.POST:
        form = ResFin(request.POST, instance=fin)
        if form.is_valid():
            resfin =form.save(commit=False)     
            fin.date_capf =  resfin.date_capf
            fin.date_capp =  resfin.date_capp
            fin.date_validation_e4 = datetime.now()
            delta = fin.date_validation_e4 - fin.date_validation_e3
            fin.delai_e4 = delta.days + 1
            if 'btn_submit' in request.POST:
                fin.etape+=1
            fin.save()
            
            return redirect('general_db')

    context={'form': form}
    return render(request, 'base/respo_fin_add.html', context)
def addfin(request, pk):
    

    form = ResFin()
    fin = GeneralDTable.objects.get(id=pk)

   

    if request.POST:
        form = ResFin(request.POST)
        if form.is_valid():
            resfin =form.save(commit=False)     
            
            fin.date_capf =  resfin.date_capf
            fin.date_capp =  resfin.date_capp
            fin.date_validation_e4 = datetime.now()
            delta = fin.date_validation_e4 - fin.date_validation_e3
            fin.delai_e4 = delta.days + 1
            if 'btn_submit' in request.POST:
                fin.etape+=1
            fin.save()
            
            return redirect('general_db')

    context={'form': form}
    return render(request, 'base/respo_fin_add.html', context)

@login_required(login_url='/login')
def updateinfo(request, pk):    
    inf = GeneralDTable.objects.get(id=pk)
    Infform = ResInf(instance = inf )
    
   
   

    if request.POST:
        Infform = ResInf(request.POST, instance=inf)
        if Infform.is_valid():
            resinf = Infform.save(commit=False)     
            
            inf.date_cacrs =  resinf.date_cacrs
          
            inf.date_validation_e5 = datetime.now()
            delta = inf.date_validation_e5 - inf.date_validation_e4
            inf.delai_e5 = delta + 1
            if 'btn_submit' in request.POST:
                inf.etape+=1
            inf.save()


            
            
        

            return redirect('general_db')

    context={'Infform': Infform }
    return render(request, 'base/respo_info_add.html', context)
def addinfo(request, pk):
    
    Infform = ResInf()
    inf = GeneralDTable.objects.get(id=pk)
    
   
   

    if request.POST:
        Infform = ResInf(request.POST)
        if Infform.is_valid():
            resinf = Infform.save(commit=False)     
            
            inf.date_cacrs =  resinf.date_cacrs
          
            inf.date_validation_e5 = datetime.now()
            delta = inf.date_validation_e5 - inf.date_validation_e4
            inf.delai_e5 = delta + 1
            if 'btn_submit' in request.POST:
                inf.etape+=1
            inf.save()


            
            
        

            return redirect('general_db')

    context={'Infform': Infform }
    return render(request, 'base/respo_info_add.html', context)




          
def export_general_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="general.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Genral Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['N Dossier','Fournisseur','Pays','Nom','Client',
    'Date du validation des conditions Logistiques','Date Validation E1', 
    'Statut Importation','Date transmission de la commande au service logistique','Code Fournisseur Sage','Reference bon de commande Sage','Catégorie commande','Date Confirmation de commande Fournisseur','Numero FP','Date FP',
    'Pays D\'origine','Incoterm','Pays Prelevement','Montant Devises','Devise','Mode Payement','Delai de livraison',
    'Execution condition payment','Date Prevu Pickup Fournisseur','Date Prevu Arrivee au maroc','Date Validation E2','Date PickUp','FreightForward','Mode Transport','Date Arrivee Maroc','Transiter',
    'Montant dedouanement dh','Date livraison Depot','Date livraison client','Litige','Classe Litige','Date Validation E3',
    'Date clôture Administrative du Payement Fournisseur','Date clôture administrative du Payement des Partenaires','Date Validation E4','Date Clôture Administrative du Cout de Revient Sage','Date Validation E5' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    rows = GeneralDTable.objects.all().values_list('n_Dossier','fournisseur','pays','nom','client','date_VCL','date_validation_e1', 
     'statut_Imp','date_TCS','code_Four_Sage','ref_Bon_Cmd_Sage','cat_Cmd','date_CCF','n_FP','date_FP','pays_Origine','incoterm','pays_Prt','montant_Dev','devise','mode_Pay',
     'delai_Liv','Exec_Co_Pay','date_PPF','date_PAM','date_validation_e2','date_pickup','freightforward','mode_trans',
     'date_AM','transitaire','Mt_ded_dh','date_ld','date_lc','litige','class_litige','date_validation_e3','date_capf','date_capp','date_validation_e4', 
     'date_cacrs','date_validation_e5')
    print(rows)
    rows = [[x.strftime("%Y-%m-%d %H:%M") if isinstance(x, datetime) else x for x in row] for row in rows ]
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    wb.save(response)

    return response

def export_dossier_xls(request, pk):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Dossier.xls"'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Dossier Data') # this will make a sheet named Users Data

    # Sheet header, first row
    row_num = 0

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['N Dossier','Fournisseur','Pays','Nom','Client',
    'Date du validation des conditions Logistiques','Date Validation E1', 
    'Statut Importation','Date transmission de la commande au service logistique','Code Fournisseur Sage','Reference bon de commande Sage','Catégorie commande','Date Confirmation de commande Fournisseur','Numero FP','Date FP',
    'Pays D\'origine','Incoterm','Pays Prelevement','Montant Devises','Devise','Mode Payement','Delai de livraison',
    'Execution condition payment','Date Prevu Pickup Fournisseur','Date Prevu Arrivee au maroc','Date Validation E2','Date PickUp','FreightForward','Mode Transport','Date Arrivee Maroc','Transiter',
    'Montant dedouanement dh','Date livraison Depot','Date livraison client','Litige','Classe Litige','Date Validation E3',
    'Date clôture Administrative du Payement Fournisseur','Date clôture administrative du Payement des Partenaires','Date Validation E4','Date Clôture Administrative du Cout de Revient Sage','Date Validation E5' ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style) # at 0 row 0 column 

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
    dossier = GeneralDTable.objects.values_list('n_Dossier','fournisseur','pays','nom','client','date_VCL','date_validation_e1', 
     'statut_Imp','date_TCS','code_Four_Sage','ref_Bon_Cmd_Sage','cat_Cmd','date_CCF','n_FP','date_FP','pays_Origine','incoterm','pays_Prt','montant_Dev','devise','mode_Pay',
     'delai_Liv','Exec_Co_Pay','date_PPF','date_PAM','date_validation_e2','date_pickup','freightforward','mode_trans',
     'date_AM','transitaire','Mt_ded_dh','date_ld','date_lc','litige','class_litige','date_validation_e3','date_capf','date_capp','date_validation_e4', 
     'date_cacrs','date_validation_e5').get(id=pk)   
  
    row_num += 1
    for col_num in range(len(dossier)):
       

        ws.write(row_num, col_num, str(dossier[col_num]), font_style)

   
    wb.save(response)




    return response

@login_required(login_url='/login')
def General_db(request):
    general_datable_1 = GeneralDTable.objects.filter(etape = request.user.etape).values()
    general_datable_2 = GeneralDTable.objects.exclude(etape = request.user.etape).values().order_by('etape')

 
    general_datable  = []

    for x in general_datable_1:
        general_datable.append(x)
    for x in general_datable_2:
        general_datable.append(x)
    
    context = {'general_datable' : general_datable , 'nombre': len(general_datable), 'general_datable_1':general_datable_1 } 
    return render(request, 'base/general_db.html', context)

def General_dyn(request):
    champs = ConTable.objects.values_list(Upper('champ'), flat=True)
    try:
        from base.dynamic_models import BaseAdmintable
        # general_dyn = BaseAdmintable.objects.all()
        general_dyn1 = BaseAdmintable.objects.all().values()

        general_dyn = []

        for x in general_dyn1:
            for i in x:
                general_dyn.append(x[i])

    except:
        pass
   
    
    print(general_dyn)
        

    context = {'champs':champs, 'general_dyn': general_dyn} 
    return render(request, 'base/general_dyn.html', context)


def createColumn(request):

            cursor1 = connection.cursor()
            query1 = '''SELECT  COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'base_dyngt' '''
            cursor1.execute(query1)
            columnNames = [item[0] for item in cursor1.fetchall()]
            # here we have two lists one return names of column in DynGt table 
            # and the second one return column names assigned by the user  
            champs = ConTable.objects.values_list(Upper('champ'), flat=True)
            # in this step we have to rename every DynGt column by the new name asigned by user using sql queries 

            cursor = connection.cursor()
            for i in range(1,100):
                for x in range(len(champs)):
                    try:
                        query = 'ALTER TABLE base_dyngt RENAME COLUMN '+ columnNames[i] +' TO '+ champs[x] +''
                        cursor.execute(query)
                    except:
                        continue

                  
            try:
                command = 'python manage.py inspectdb  base_dyngt > base/dynamic_models.py'
                os.system(command)
                print('done1')
            except:
                print('done2')
                return redirect('general_db')
           
                   

                    
                              



            # columnname = ''
            # newcolumnname = ''
            # columntype = 'VARCHAR'
            # columnlength = '255'
        
            # cursor = connection.cursor()
            # query = 'ALTER TABLE `base_admintable` ADD COLUMN `'+columnname +'` '+ columntype + '('+columnlength+') NOT NULL'
            # query = 'ALTER TABLE base_admintable RENAME COLUMN '+columnname +' TO '+ newcolumnname +''

            # query = 'ALTER TABLE base_admintable DROP COLUMN '+columnname +''ALTER TABLE users RENAME COLUMN id TO user_id;
            # cursor.execute(query)



            # try:
            #     command = 'python manage.py inspectdb  base_admintable > base/dynamic_models.py'
            #     os.system(command)
            #     print('done1')
            # except:
            #     print('done2')
            #     return redirect('general_db')



            return render(request, 'base/general.html')
            
#Dynamic Part 
def add_admin_table(request):
    
    form = AdminForm()

    if request.POST:
        form = AdminForm(request.POST)
        if form.is_valid():
            conf =form.save(commit=False)  
            conf.column+= 1

            form.save()

            columnname = form.cleaned_data.get('champ')
            columntype = form.cleaned_data.get('type')
            columnlength = '255'
        
            cursor = connection.cursor()
            if columntype == 'DATE':
                query = 'ALTER TABLE `base_admintable` ADD COLUMN `'+columnname +'` '+ columntype + ''
            else:
                query = 'ALTER TABLE `base_admintable` ADD COLUMN `'+columnname +'` '+ columntype + '('+columnlength+') NOT NULL'                                                                                                   

            cursor.execute(query)

    #  in this step i try to use inspectdb command after the user save the configform 
            try:
                command = 'python manage.py inspectdb  base_admintable > base/dynamic_models.py'
                os.system(command)
                print('done1')   
            except:
                pass
            


    context = {'configform': form}
    return render(request, 'base/createEtape.html', context)



def manage_dyanmic(request):
    
    p = ConTable.objects.filter(etape = request.user.etape)
    champs = ConTable.objects.filter(etape = request.user.etape).values_list('champ', flat=True)
    etappe = Etapes.objects.get(numero = request.user.etape)
    print(etappe.numero)

    #passing the object to the form
    formset = DynForm(x = p)
 

    if request.POST:
        formset = DynForm(request.POST, x=p)
        if formset.is_valid():
            # Create an empty list to store the cleaned data
            values = []


            # Loop through the "champs" list
            for x in champs:  
                # Retrieve the cleaned data for each "champ" value
                data = formset.cleaned_data.get(x)

                # Append the cleaned data to the "values" list
                values.append(data)
            # Execute the SQL INSERT statement using the cursor
            with connection.cursor() as cursor:
                # Use the "champs" list to generate the column names in the INSERT statement
                columns = ",".join(champs)
                print(columns)
                # Use the "values" list to generate the VALUES placeholder in the INSERT statement
                placeholders = ",".join(["%s"] * len(values))
                print(placeholders)
                cursor.execute("INSERT INTO base_admintable ("+ columns +") VALUES ("+ placeholders +")", values)

            if etappe.numero == request.user.etape:
                etappe.date_validation = datetime.now()
                etappe.save()

                print(etappe.date_validation)


            return redirect('general_dyn')
    
    return render(request, 'base/add_new.html', {'formset': formset})





def add_admin_champs(request):
    form = EtapeForm(request.POST)
    # champss = Etapes.objects.all()
    if request.method == 'POST':
        
        if form.is_valid():

            form.save()
            return redirect('add_etape')



    return render(request, 'base/add_etape.html', context={'form': form})
