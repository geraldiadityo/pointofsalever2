# Generated by Django 3.2.11 on 2022-02-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stok', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stokm',
            name='expired_date',
            field=models.DateField(null=True),
        ),
    ]
