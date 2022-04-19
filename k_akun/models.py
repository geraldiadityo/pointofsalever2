from django.db import models

# Create your models here.
class Akun(models.Model):
    nama_akun = models.CharField(max_length=50, null=True, blank=True)
    kode_akun = models.CharField(max_length=20, null=True,blank=True)
    KATEGORI_TYPE = (
        ('Debet','Debet'),
        ('Kredit','Kredit'),
    )
    kategori = models.CharField(max_length=10, null=True, choices=KATEGORI_TYPE)

    def __str__(self):
        return "{}".format(self.nama_akun)

