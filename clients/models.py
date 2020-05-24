from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django_countries.fields import CountryField
from django.urls import reverse
from product.models import Order

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,
    on_delete=models.CASCADE , verbose_name=_("User"))
    firstname = models.CharField(max_length=20,blank=True,null=True)
    lastname = models.CharField(max_length=20,blank=True,null=True)
    email =  models.CharField(max_length=50)
    picture = models.ImageField(default='default.png', upload_to='profile_pics',blank=True,null=True)
    phone = models.CharField(max_length=30,blank=True,null=True)
    Tel   = models.CharField(max_length=30 ,blank=True,null=True)
    address = models.ManyToManyField('Address',verbose_name=_("Address"),blank=True)

    
    def __str__(self):
        return self.user.username
    
    def getAddresses(self):
        addresses = []
        for address in self.address.all():
            addresses.append(address)
        return addresses

    def get_default_address(self): 
        default_pk = None
        for address in self.address.all():
            if address.default:
                default_pk = address.pk
        return default_pk
    
    def getTotalOrders(self):
        orders = Order.objects.filter(user=self.user)
        return len(orders)


@receiver(user_signed_up)
def create_profile(sender, **kwargs):
    profile = Profile.objects.create(user=kwargs['user'])
    profile.save()


class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,
    on_delete=models.CASCADE , verbose_name=_("User"))
    street_address = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100,blank=True,null=True)
    zipCode = models.CharField(max_length=100)
    country = CountryField()
    city = models.CharField(max_length=50, blank=True, null=True)
    default = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    class Meta:
        verbose_name = _("Address")
        verbose_name_plural = _("Addresses")
    
    def get_absolute_url(self):
        return reverse("clients:edit-address", kwargs={"pk": self.pk})
