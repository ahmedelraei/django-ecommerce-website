# Generated by Django 3.0.5 on 2020-05-16 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_remove_address_address_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='firstname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='lastname',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]