from django.db import models

# Create your models here.
class EmployeeData(models.Model):
    Emp_Id = models.IntegerField(primary_key=True)
    Emp_Name=models.CharField(max_length=30)
    Date= models.DateField()
    Check_In=models.TimeField()
    Check_Out=models.TimeField()

    def __str__(self):
        return self.Emp_Name