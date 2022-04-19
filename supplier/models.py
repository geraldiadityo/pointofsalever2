from django.db import models

# Create your models here.
class Supplier(models.Model):
    nama = models.CharField(max_length=200,blank=True,null=True)
    telp = models.CharField(max_length=15,blank=True,null=True)
    alamat = models.TextField()
    deskripsi = models.TextField()
    created = models.DateTimeField(auto_now_add=True,editable=False,null=True)

    def __str__(self):
        return "{}".format(self.nama)
