from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=20)
    email = models.CharField(max_length=80)
    password = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    address = models.CharField(max_length = 40)
    last_login = models.DateTimeField
    createdtime = models.DateTimeField
    updatedtime = models.DateTimeField
    deletedtime = models.DateTimeField
    deleted = models.IntegerField(default=0)
    
class Spending(models.Model):
    id = models.AutoField(primary_key=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    amount = models.IntegerField
    createdtime = models.DateTimeField
    updatedtime = models.DateTimeField
    deletedtime = models.DateTimeField
    deleted = models.IntegerField(default=0)
    