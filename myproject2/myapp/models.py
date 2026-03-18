from django.db import models


class Member(models.Model):
  firstname = models.CharField(max_length=255)
  middlename = models.CharField(max_length=255, null=True)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  
  def __str__(self):
    return self.firstname



# Create your models here.
