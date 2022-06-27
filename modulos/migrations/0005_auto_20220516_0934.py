# Generated by Django 3.0.3 on 2022-05-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0004_modulos'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulos',
            name='nombre',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='NombreModulo'),
        ),
        migrations.AlterField(
            model_name='modulos',
            name='mac',
            field=models.CharField(max_length=11, primary_key=True, serialize=False, verbose_name='MAC'),
        ),
    ]
