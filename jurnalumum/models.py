from django.db import models

# Create your models here.
from k_akun.models import Akun

class Jurnal(models.Model):
    tgl = models.DateField(null=True, blank=True)
    akun = models.ForeignKey(Akun, null=True, on_delete=models.SET_NULL)
    ket = models.TextField()
    ref = models.CharField(max_length=50,null=True,blank=True)
    nominal = models.IntegerField(null=True,blank=True)
    TYPE_LIST = (
        ('Debet','Debet'),
        ('Kredit','Kredit'),
    )
    
    tipe = models.CharField(max_length=20,choices=TYPE_LIST)

    def __str__(self):
        return "{}".format(self.tgl)
    

