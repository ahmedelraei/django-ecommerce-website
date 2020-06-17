# Generated by Django 3.0.5 on 2020-06-16 22:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payment', '0005_payment_sender'),
        ('clients', '0014_auto_20200604_1437'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('settings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CATname', models.CharField(max_length=50, verbose_name='Name:')),
                ('CATdesc', models.TextField(max_length=5000)),
                ('CATimg', models.ImageField(blank=True, null=True, upload_to='category/')),
                ('CATslug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='URL:')),
                ('CATparent', models.ForeignKey(blank=True, limit_choices_to={'CATparent__isnull': True}, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='Main Category:')),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='MainSlider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SDRimg', models.ImageField(upload_to='MainSlider/', verbose_name='Slide:')),
            ],
            options={
                'verbose_name': 'Slide',
                'verbose_name_plural': 'Main Slider',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDname', models.CharField(max_length=100, verbose_name='Name:')),
                ('PRDdesc', tinymce.models.HTMLField(max_length=20000, verbose_name='Description')),
                ('PRDdetails', tinymce.models.HTMLField(blank=True, max_length=20000, null=True, verbose_name='Details')),
                ('PRDshipping_notes', models.TextField(blank=True, max_length=5000, null=True, verbose_name='Shipping Details')),
                ('PRDshipping_regions', django_countries.fields.CountryField(max_length=746, multiple=True, verbose_name='Shipping Regions')),
                ('PRDimage', models.ImageField(blank=True, null=True, upload_to='productimg/', verbose_name='Image:')),
                ('PRDprice', models.DecimalField(decimal_places=3, max_digits=20, verbose_name='Price:')),
                ('PRDdiscount', models.DecimalField(decimal_places=3, default=0, max_digits=20, verbose_name='After Discount:')),
                ('PRDcost', models.DecimalField(decimal_places=3, max_digits=20, verbose_name='Cost:')),
                ('stock_quantity', models.IntegerField(default=1, verbose_name='In Stock:')),
                ('PRDcreated', models.DateTimeField(verbose_name='Created at:')),
                ('PRDslug', models.SlugField(blank=True, max_length=255, null=True, unique=True, verbose_name='URL:')),
                ('PRDisNew', models.BooleanField(default=True, verbose_name='NEW:')),
                ('PRDisTrend', models.BooleanField(default=False, verbose_name='Trending:')),
                ('PRDbrand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='settings.Brand', verbose_name='Brand')),
                ('PRDcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PRDcat', to='product.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='ProductImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PRDImage', models.ImageField(blank=True, null=True, upload_to='productimg/', verbose_name='Image:')),
                ('PRD', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product', verbose_name='Product:')),
            ],
        ),
        migrations.CreateModel(
            name='Product_Alternatives',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PALalternatives', models.ManyToManyField(related_name='alternative_products', to='product.Product', verbose_name='Alternative Product:')),
                ('PALproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='main_product', to='product.Product', verbose_name='Product:')),
            ],
            options={
                'verbose_name': 'Product Alternative',
                'verbose_name_plural': 'Product Alternatives',
            },
        ),
        migrations.CreateModel(
            name='Product_Accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PACCaccessories', models.ManyToManyField(related_name='accessories_products', to='product.Product', verbose_name='Accessories Products:')),
                ('PACCproduct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mainAccessory_product', to='product.Product', verbose_name='Main Accessory:')),
            ],
            options={
                'verbose_name': 'Product Accessory',
                'verbose_name_plural': 'Product Accessories',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False, verbose_name='Order item State')),
                ('quantity', models.IntegerField(default=1)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('listed_date', models.DateTimeField(auto_now_add=True, verbose_name='Listed Date')),
                ('ordered_date', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Ordered Date')),
                ('ordered', models.BooleanField(default=False, editable=False, verbose_name='Ordered')),
                ('order_ref', models.CharField(editable=False, max_length=20, unique=True)),
                ('orderTotal', models.FloatField(default=0, editable=False, verbose_name='Total')),
                ('pending', models.BooleanField(default=True)),
                ('processing', models.BooleanField(default=False)),
                ('cancelled', models.BooleanField(default=False)),
                ('shipped', models.BooleanField(default=False)),
                ('delivered', models.BooleanField(default=False)),
                ('items', models.ManyToManyField(to='product.OrderItem', verbose_name='Products')),
                ('payment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.Payment', verbose_name='Payment')),
                ('shippingAddress', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='shippingAddress', to='clients.Address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
    ]
