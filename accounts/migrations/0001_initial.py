# Generated by Django 3.0.5 on 2020-04-14 23:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picture', models.ImageField(blank=True, default='default.png', null=True, upload_to='profile_pics')),
                ('street_address', models.CharField(max_length=100)),
                ('apartment', models.CharField(max_length=100)),
                ('address2', models.CharField(max_length=100)),
                ('phone', phone_field.models.PhoneField(max_length=31)),
                ('Tel', phone_field.models.PhoneField(blank=True, max_length=31, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
