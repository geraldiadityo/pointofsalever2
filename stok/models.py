from django.db import models

# Create your models here.
from supplier.models import Supplier
from p_item.models import Item_p

class StokM(models.Model):
    TIPE = (
        ('in','IN'),
        ('out','OUT'),
    )
    product = models.ForeignKey(Item_p, null=True,blank=True,on_delete=models.SET_NULL)
    tipe = models.CharField(max_length=20,null=True,choices=TIPE)
    detail = models.TextField()
    supplier = models.ForeignKey(Supplier, null=True,blank=True,on_delete=models.SET_NULL)
    hargabeli = models.IntegerField(null=True,blank=True,default=0)
    qty = models.IntegerField(null=True,blank=True)
    total = models.IntegerField(null=True,blank=True)
    expired_date = models.DateField(null=True,editable=True)
    tanggal = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return "{}. {}".format(self.id,self.tipe)

