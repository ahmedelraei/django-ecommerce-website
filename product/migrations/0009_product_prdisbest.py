# Generated by Django 3.0.5 on 2020-04-17 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20200417_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='PRDisBest',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
