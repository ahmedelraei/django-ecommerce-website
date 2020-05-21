# Generated by Django 3.0.5 on 2020-05-16 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0011_remove_address_address_type'),
        ('product', '0030_auto_20200516_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='billing_address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='billing_address', to='clients.Address'),
        ),
        migrations.AlterField(
            model_name='order',
            name='shippingAddress',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shippingAddress', to='clients.Address'),
        ),
    ]
