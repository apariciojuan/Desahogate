# Generated by Django 2.1.2 on 2018-11-23 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entradas', '0002_auto_20181122_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='records',
            old_name='Descripcion',
            new_name='descripcion',
        ),
    ]
