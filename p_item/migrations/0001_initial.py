# Generated by Django 3.2.11 on 2022-01-28 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('p_unit', '0001_initial'),
        ('p_kategori', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item_p',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('barcode', models.CharField(blank=True, max_length=200, null=True)),
                ('nama', models.CharField(blank=True, max_length=200, null=True)),
                ('stok', models.IntegerField(default=0, editable=False)),
                ('hargaawal', models.BigIntegerField(blank=True, default=0, null=True)),
                ('harga', models.BigIntegerField(blank=True, default=0, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('slug', models.SlugField(editable=False, null=True)),
                ('kategori', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='p_kategori.kategori_p')),
                ('unit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='p_unit.unit_p')),
            ],
        ),
    ]
