# Generated by Django 3.0.5 on 2020-05-16 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0012_auto_20200516_1041'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.CharField(default='ahmed@mail.com', max_length=50),
            preserve_default=False,
        ),
    ]
