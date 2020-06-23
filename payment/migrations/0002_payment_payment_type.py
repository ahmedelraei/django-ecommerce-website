# Generated by Django 3.0.5 on 2020-06-04 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('C', 'Cash'), ('F', 'Fawry'), ('W', 'e-Wallet')], default='C', max_length=1),
            preserve_default=False,
        ),
    ]