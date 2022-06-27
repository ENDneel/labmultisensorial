# Generated by Django 2.2.10 on 2022-01-04 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Serios',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tiempo', models.CharField(max_length=15, verbose_name='fecha')),
                ('duracion', models.PositiveIntegerField(default=0, verbose_name='duracion')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]