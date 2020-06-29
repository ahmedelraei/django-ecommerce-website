# -*- coding: utf-8 -*-
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
from django.conf import settings
from project.settings import BASE_DIR
from django_countries.fields import CountryField
from tinymce import models as tinymce_models
from django.conf.urls.static import static
import os
import uuid
from PIL import Image as _img
from io import BytesIO

class Product(models.Model):
    PRDname  = models.CharField(max_length=100, verbose_name=_("Name:"))
    PRDcategory = models.ForeignKey('Category',related_name='PRDcat', on_delete=models.CASCADE,blank=True, null=True,verbose_name=_("Category"))
    PRDbrand    = models.ForeignKey('settings.Brand',on_delete=models.CASCADE,blank=True, null=True,verbose_name=_("Brand"))
    PRDdesc  = tinymce_models.HTMLField(verbose_name=_("Description"))
    PRD_SEO_desc = models.TextField(max_length=300,verbose_name=_("SEO Description"),blank=True, null=True) 
    PRDtags = models.TextField(max_length=300,verbose_name=_("SEO Tags"),blank=True, null=True) 
    PRDdetails = tinymce_models.HTMLField(verbose_name=_("Details"),blank=True, null=True)
    PRDshipping_notes = models.TextField(max_length=5000,verbose_name=_("Shipping Details"),blank=True, null=True)
    PRDshipping_regions = CountryField(multiple=True,verbose_name=_("Shipping Regions"))
    PRDimage = models.ImageField(upload_to='productimg/',verbose_name=_("Image:"),blank=True, null=True)
    PRDprice = models.DecimalField(max_digits=20,decimal_places=3,verbose_name=_("Price:"))
    PRDdiscount = models.DecimalField(max_digits=20,decimal_places=3,verbose_name=_("After Discount:") ,default=0)    
    PRDcost  = models.DecimalField(max_digits=20,decimal_places=3,verbose_name=_("Cost:"))
    stock_quantity = models.IntegerField(default=1,verbose_name=_("In Stock:"))
    PRDcreated = models.DateTimeField(verbose_name=_("Created at:"))
    PRDslug    = models.SlugField(max_length=255,unique=True,blank=True, null=True, verbose_name=_("URL:"),allow_unicode=True)
    PRDisNew = models.BooleanField(default=True, verbose_name=_("NEW:"))
    PRDisTrend = models.BooleanField(default=False,verbose_name=_("Trending:"))

    def save(self, *args, **kwargs):
        if not self.PRDslug:
            self.PRDslug = slugify(self.PRDname, allow_unicode=True)
        if self.PRDimage:
            image = _img.open(BytesIO(self.PRDimage.read()))
            output = BytesIO()
            image.save(output, format='webp')
            output.seek(0)
            self.PRDimage = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.PRDslug, 'image/webp',output.tell(), None)

        super(Product,self).save(*args, **kwargs)
        
        
            
    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        print(self.PRDslug,"##################################")
        return reverse("products:product_details", kwargs={"str": self.PRDslug})
    
    def get_addToCart_url(self):
        print(self.PRDslug,"##################################")
        return reverse("products:add-to-cart", kwargs={"str": self.PRDslug})

    def get_removeFromCart_url(self):
        print(self.PRDslug,"##################################")
        return reverse("products:remove-from-cart", kwargs={"str": self.PRDslug})

    def getPrice(self):
        if self.PRDdiscount:
            return self.PRDdiscount
        else:
            return self.PRDprice

    def GetMainimg(self):
        if self.PRDimage:
            return self.PRDimage.url
        else:
            img = os.path.join("/static/site_static/img/default.png")
            return img

    def get_shipping_regions(self):
        country_list = []
        for country in self.PRDshipping_regions:
            country_list.append(str(country.name))
        return country_list

    def __str__(self):
        return self.PRDname

class ProductImage(models.Model):
    PRD = models.ForeignKey(Product , on_delete=models.CASCADE,verbose_name=_("Product:"),blank=True, null=True)
    PRDImage = models.ImageField(upload_to='productimg/',verbose_name=_("Image:"),blank=True, null=True)
    
    def __str__(self):
        return str(self.PRD)
    
    def save(self, *args, **kwargs):
        if self.PRDImage:
            image = _img.open(BytesIO(self.PRDImage.read()))
            output = BytesIO()
            image.save(output, format='webp')
            output.seek(0)
            self.PRDImage = InMemoryUploadedFile(output,'ImageField', "%s.webp" %self.PRD.PRDslug, 'image/webp',output.tell(), None)

        super(ProductImage,self).save(*args, **kwargs)

class MainSlider(models.Model):
    SDRimg = models.ImageField(upload_to='MainSlider/',verbose_name=_("Slide:"))

    class Meta:
        verbose_name = _("Slide")
        verbose_name_plural = _("Main Slider")

    def __str__(self):
        title = "Slide | " + str(self.SDRimg).split("/")[1]
        return title

class Category(models.Model):
    CATname = models.CharField(max_length=50,verbose_name=_("Name:"),blank=False, null=False)
    CATparent  = models.ForeignKey('self',limit_choices_to={'CATparent__isnull':True},on_delete=models.CASCADE,verbose_name=_("Main Category:"),blank=True, null=True)
    CATdesc  = models.TextField(max_length=5000,)
    CATimg   = models.ImageField(upload_to='category/',blank=True, null=True)
    CATslug  = models.SlugField(max_length=255,unique=True,blank=True, null=True, verbose_name=_("URL:"), allow_unicode=True)


    def save(self, *args, **kwargs):
        if not self.CATslug:
            self.CATslug = slugify(self.CATname, allow_unicode=True)
            super(Category,self).save(*args, **kwargs)
        else:
            super(Category,self).save(*args, **kwargs)
            

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")


    def __str__(self):
        return self.CATname


class Product_Alternatives(models.Model):
    PALproduct = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="main_product",verbose_name=_("Product:"))
    PALalternatives = models.ManyToManyField(Product,related_name="alternative_products",verbose_name=_("Alternative Product:"))

    

    class Meta:
        verbose_name = _("Product Alternative")
        verbose_name_plural = _("Product Alternatives")

    def __str__(self):
        return str(self.PALproduct)

class Product_Accessories(models.Model):
    PACCproduct = models.ForeignKey(Product,on_delete=models.CASCADE,related_name="mainAccessory_product",verbose_name=_("Main Accessory:"))
    PACCaccessories = models.ManyToManyField(Product,related_name="accessories_products",verbose_name=_("Accessories Products:"))
    

    class Meta:
        verbose_name = _("Product Accessory")
        verbose_name_plural = _("Product Accessories")

    def __str__(self):
        return str(self.PACCproduct)

class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,
    on_delete=models.CASCADE, verbose_name=_("User"))
    ordered = models.BooleanField(default=False,verbose_name=_("Order item State"))   
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    #item_variation = models.ManyToManyField('ItemVariation')
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.quantity} of {self.item.PRDname}"

    def getTotalDiscountItemPrice(self):
        return self.quantity * self.item.PRDdiscount

    def getTotalItemPrice(self):
        return self.quantity * self.item.PRDprice

    def getFinalPrice(self):
        if self.item.PRDdiscount:
            return self.getTotalDiscountItemPrice()
        else:
            return self.getTotalItemPrice()
    
    def getSavedPercent(self):
        saved_percent = 100 - round((self.item.PRDdiscount/self.item.PRDprice)*100)
        saved = str(saved_percent) + "%"
        return saved

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,
    on_delete=models.CASCADE , verbose_name=_("User"))
    items = models.ManyToManyField(OrderItem ,verbose_name=_("Products"))
    listed_date = models.DateTimeField(auto_now_add=True , verbose_name=_("Listed Date"),editable=False)
    ordered_date = models.DateTimeField(blank=True,null=True,verbose_name=_("Ordered Date"),editable=False)
    ordered = models.BooleanField(default=False,verbose_name=_("Ordered"),editable=False)
    order_ref = models.CharField(max_length=20,unique=True,editable=False)
    payment = models.ForeignKey('payment.Payment',blank=True, null=True,verbose_name=_('Payment'),on_delete=models.CASCADE)
    orderTotal = models.FloatField(default=0,editable=False,verbose_name=_("Total"))
    shippingAddress = models.ForeignKey('clients.Address',related_name="shippingAddress",on_delete=models.SET_NULL,blank=True,null=True)
    pending = models.BooleanField(default=True)
    processing = models.BooleanField(default=False)
    cancelled = models.BooleanField(default=False)
    shipped = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    def getTotal(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.getFinalPrice()
        return total
    
    def getState(self):
        if self.delivered:
            return "Delivered"
        elif self.shipped:
            return "Shipped"
        else:
            return "Processing"
    
    def get_cancel_url(self):
        return reverse('clients:cancel-order',kwargs={'code':self.order_ref})
    

class Variation(models.Model):
    item = models.ForeignKey(Product,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    class Meta:
        unique_together = (
            ('item' , 'name'),
        )
    
    def __str__(self):
        return self.name

class ItemVariation(models.Model):
    variation = models.ForeignKey(Variation,on_delete=models.CASCADE)
    value = models.CharField(max_length=100)
    image = models.ImageField()

    class Meta:
        unique_together = (
            ('variation' , 'value'),
        )
        
    def __str__(self):
        return self.name