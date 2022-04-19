from django.db import models
from django.utils.text import slugify

# Create your models here.
from p_kategori.models import Kategori_p
from p_unit.models import Unit_p

class Item_p(models.Model):
    barcode = models.CharField(max_length=200,null=True,blank=True)
    nama = models.CharField(max_length=200,null=True,blank=True)
    kategori = models.ForeignKey(Kategori_p, null=True,on_delete=models.SET_NULL)
    unit = models.ForeignKey(Unit_p, null=True,on_delete=models.SET_NULL)
    stok = models.IntegerField(default=0,editable=False)
    hargaawal = models.BigIntegerField(default=0,null=True,blank=True)
    harga = models.BigIntegerField(default=0,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,null=True,editable=False)
    slug = models.SlugField(null=True,editable=False)

    def save(self):
        self.slug = slugify(self.nama)
        super().save()
    
    def __str__(self):
        return "{}".format(self.nama)

