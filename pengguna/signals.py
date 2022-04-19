from django.db.models.signals import post_save
from django.contrib.auth.models import User,Group

from .models import Pengguna

def pengguna_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='kasir')
        instance.groups.add(group)
        Pengguna.objects.create(
            user=instance,
            nama=instance.username,
            email=instance.email,
        )

post_save.connect(pengguna_profile,sender=User)
