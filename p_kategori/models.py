from django.db import models

# Create your models here.
class Kategori_p(models.Model):
    nama = models.CharField(max_length=200,blank=True,null=True)

    def __str__(self):
        return "{}".format(self.nama)

