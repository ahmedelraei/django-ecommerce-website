# Generated by Django 3.0.5 on 2020-05-13 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0009_auto_20200513_0857'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='address',
            field=models.ManyToManyField(blank=True, null=True, to='clients.Address', verbose_name='Address'),
        ),
    ]