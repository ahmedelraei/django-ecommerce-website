# Generated by Django 3.0.5 on 2020-08-30 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_auto_20200830_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDcreated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created at:'),
        ),
    ]
