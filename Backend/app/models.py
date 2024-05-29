from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=250)
    Email=models.EmailField()
    Password=models.CharField(max_length=250)

    class Meta():
        db_table='Student'
        verbose_name_plural='Student'