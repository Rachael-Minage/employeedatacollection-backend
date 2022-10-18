from django.db import models

# Create your models here.

from datetime import datetime
from django.db import models


# Create your models here.
class Employee(models.Model):
    first_name = models.CharField(primary_key=True,max_length=24)
    middle_name = models.CharField(max_length=26,blank=True) 
    date_of_graduation = models.DateField(null=True)
    date_of_employment = models.DateField(null=True)
    position = models.CharField(max_length=20,blank=True)
    salary = models.IntegerField(default=True)
    supervisors = models.CharField(max_length=26,blank=True)
    
    @property
    def employee_code(self):
        import random
        random_number = random.randint(100,900)
        initials_one = self.first_name[0].upper()
        initials_two = self.middle_name[0].upper()
        initials ='%s%s%s'%(random_number,initials_one,initials_two)
        return initials



