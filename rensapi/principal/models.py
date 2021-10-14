from django.db import models

# Create your models here.

class Principal(models.Model):
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    member_type= models.CharField(max_length=30)
    member_number= models.CharField(max_length=30)

class Dependants(models.Model):
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    member_type= models.CharField(max_length=30)
    principal_no = models.ForeignKey(Principal, null= False, on_delete=models.CASCADE)