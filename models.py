from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Education(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    username=models.CharField(max_length=255,null=True)
    name=models.CharField(max_length=255,null=True)
    email=models.CharField(max_length=200,null=True)
    phn=models.DecimalField(max_digits=10,decimal_places=0,default=0)

    def __str__(self):
        return self.username