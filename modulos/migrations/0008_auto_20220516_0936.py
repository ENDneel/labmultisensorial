# Generated by Django 3.0.3 on 2022-05-16 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0007_auto_20220516_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulos',
            name='nombre',
            field=models.CharField(blank=True, max_length=30, verbose_name='NombreModulo'),
        ),
    ]
