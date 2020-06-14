# Generated by Django 3.0.5 on 2020-06-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0038_auto_20200523_1126'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='paid',
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.CharField(default='C', editable=False, max_length=1, verbose_name='payment'),
            preserve_default=False,
        ),
    ]
