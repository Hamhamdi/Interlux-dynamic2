# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class BaseAdmintable(models.Model):
    id = models.BigAutoField(primary_key=True)
    etape = models.IntegerField()
    user_id = models.IntegerField(unique=True)
    field_user_name_field = models.CharField(db_column="'user_name'", max_length=255)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_age_field = models.CharField(db_column="'age'", max_length=255)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_name_field = models.CharField(db_column="'name'", max_length=255)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    field_client_field = models.CharField(db_column="'client'", max_length=255)  # Field renamed to remove unsuitable characters. Field renamed because it started with '_'. Field renamed because it ended with '_'.
    find = models.CharField(max_length=255)
    me = models.CharField(max_length=255)
    fournisseur = models.CharField(max_length=255)
    datep = models.CharField(max_length=255)
    datepp = models.CharField(max_length=255)
    datpp = models.CharField(max_length=255)
    atpp = models.CharField(max_length=255)
    tpp = models.CharField(max_length=255)
    tprp = models.CharField(max_length=255)
    tprpd = models.CharField(max_length=255)
    tprrpd = models.CharField(max_length=255)
    tprerpd = models.CharField(max_length=255)
    tpd = models.CharField(max_length=255)
    tpf = models.CharField(max_length=255)
    tpr = models.CharField(max_length=255)
    tprt = models.CharField(max_length=255)
    tprttt = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'base_admintable'
