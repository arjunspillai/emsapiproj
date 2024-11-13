from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from rest_framework.authtoken.models import Token
# Create your models here.

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)
        

# Create a Department model class by inheriting the model class
class Department(models.Model):
    #Department is auto incrementing and is primary key
    DepartmentID = models.AutoField(primary_key=True)
    #Department name is char field with maximum char length of 200
    DepartmentName = models.CharField(max_length=200)

#whenever we try to print the dept object,
#instead of 

    def __str__(self):
        return self.DepartmentName


class Employee(models.Model):
     
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=200)
    Designation = models.CharField(max_length=200)
    DateOfJoining = models.DateField()
     #depid is a foreign key from the dept model
    DepartmentID = models.ForeignKey(Department,on_delete=models.CASCADE)
    Contact = models.CharField(max_length=200)
    ISActive = models.BooleanField(default=True)

    def __str__(self):
     return self.EmployeeName