
from django.db import models

# Create your models here.
class Principal(models.Model):
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    member_type= models.CharField(max_length=30)
    member_number= models.CharField(max_length=30)


    def __str__(self):
        return self.first_name+' '+self.last_name
    
class Dependants(models.Model):
    first_name= models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    member_type= models.CharField(max_length=30)
    principal_no = models.ForeignKey(Principal,related_name='dependants', null= False, on_delete=models.CASCADE)


    def __str__(self):
        return self.first_name+' '+self.last_name
    


