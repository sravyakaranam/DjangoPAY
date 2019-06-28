from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.
class Account(models.Model):
    accChoice=(
        ('1','Savings'),
        ('2','Current')
    )
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,help_text="generated unique id for user")
    AccountUser=models.CharField(max_length=100,help_text='user name',null=True)
    # name=models.CharField(max_length=100,null=True)
    typeaccount=models.CharField(max_length=100, help_text='type of account',choices=accChoice,null=True)
    
    balance=models.IntegerField(default=0)

    def __str__(self):
        return self.AccountUser
    # class Meta:
    #     ordering = ['user']

# class Person(models.Model):
#     person_name=models.ForeignKey(User,on_delete=models.CASCADE)
    # class Meta:
    #      ordering = ['person_name']