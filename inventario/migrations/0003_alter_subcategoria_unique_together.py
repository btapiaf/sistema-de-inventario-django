# Generated by Django 3.2.6 on 2021-08-30 18:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventario', '0002_auto_20210830_1332'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='subcategoria',
            unique_together={('categoria', 'descripcion')},
        ),
    ]
