from . import views
from django.urls import path

urlpatterns = [


    path('', views.home, name="home" ),
    path('logout/', views.logoutUser, name="logout" ),
    path('login/', views.loginPage, name="login" ),
    path('register/', views.registerPage, name="register" ),
    
    path('respo_ca_add/', views.addRCa, name="respo_ca_add" ),
    path('update_ca/<str:pk>/', views.updateRCa, name="update_ca" ),

    path('respo_log1_add/<str:pk>/', views.addlog1, name="respo_log1_add" ),
    path('update_log1/<str:pk>/', views.updatelog1, name="update_log1" ),


    path('respo_log2_add/<str:pk>/', views.addlog2, name="respo_log2_add" ),
    path('update_log2/<str:pk>/', views.updatelog2, name="update_log2" ),


    path('respo_fin_add/<str:pk>/', views.addfin, name="respo_fin_add" ),
    path('update_fin/<str:pk>/', views.updatefin, name="update_fin" ),

    path('respo_info_add/<str:pk>/', views.addinfo, name="respo_info_add" ),
    path('update_info/<str:pk>/', views.updateinfo, name="update_info" ),

    path('general_db/', views.General_db, name="general_db" ),
    path('general_dyn/', views.General_dyn, name="general_dyn" ),
    path('admin_table_add/', views.add_admin_table, name="admin_table_add" ),
    path('add_new/', views.manage_dyanmic, name="add_new"),


    # path('admin_table_add/', views.createColumn, name="admin_table_add" ),

    path('generalfile', views.export_general_xls, name="generalfile"), 
    path('dossier/<str:pk>/', views.export_dossier_xls, name="dossier"), 
    path('add_admin_champs/', views.add_admin_champs, name="add_etape" ),



]