# Generated by Django 3.0.5 on 2020-06-28 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_orderitem_item_var'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='item_var',
        ),
    ]
