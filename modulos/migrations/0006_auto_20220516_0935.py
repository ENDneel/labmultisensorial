# Generated by Django 3.0.3 on 2022-05-16 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_auto_20220516_0934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulos',
            name='nombre',
            field=models.CharField(max_length=30, verbose_name='NombreModulo'),
        ),
    ]
