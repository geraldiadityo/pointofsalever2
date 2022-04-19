from django.db import models

from p_item.models import Item_p

# Create your models here.

class SaleModel(models.Model):
    invoice = models.CharField(max_length=50,null=True)
    totalharga = models.IntegerField()
    discount = models.IntegerField()
    total_bayar = models.IntegerField()
    total_pendapatan = models.IntegerField(null=True,default=0,blank=True)
    cash = models.IntegerField()
    kembalian = models.IntegerField()
    note = models.TextField(null=True,blank=True)
    tanggal = models.DateField(auto_now_add=True,null=True)
    created = models.DateTimeField(auto_now_add=True,editable=False,blank=True)

    def __str__(self):
        return "{}. {}".format(self.id,self.invoice)
    

class KeranjangModel(models.Model):
    product = models.ForeignKey(Item_p,null=True, on_delete=models.SET_NULL)
    qty = models.IntegerField()
    discount = models.IntegerField(null=True)
    totalharga = models.IntegerField()
    total_untung = models.IntegerField(default=0,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True,editable=False)


    def __str__(self):
        return "{}".format(self.id)


