# Generated by Django 3.0.5 on 2020-05-13 01:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0007_profile_address'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='address',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.ManyToManyField(to='clients.Address', verbose_name='Address'),
        ),
    ]
