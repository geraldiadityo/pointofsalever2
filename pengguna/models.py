from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pengguna(models.Model):
    user = models.OneToOneField(User, null=True,blank=True,on_delete=models.CASCADE)
    nama = models.CharField(max_length=200,null=True)
    phone = models.CharField(max_length=20,null=True)
    email = models.CharField(max_length=200,null=True)
    profile_pic = models.ImageField(default='profile1.png',null=True,blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "{}".format(self.nama)
