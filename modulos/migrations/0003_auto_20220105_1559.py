# Generated by Django 2.2.10 on 2022-01-05 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_auto_20220104_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serios',
            name='fecha',
            field=models.CharField(max_length=30, null=True, verbose_name='fecha'),
        ),
    ]