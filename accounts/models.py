from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from allauth.account.signals import user_signed_up

class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL ,
    on_delete=models.CASCADE , verbose_name=_("User"))
    picture = models.ImageField(default='default.png', upload_to='profile_pics',blank=True,null=True)
    street_address = models.CharField(max_length=100,blank=True,null=True)
    apartment = models.CharField(max_length=100,blank=True,null=True)
    address2  = models.CharField(max_length=100,blank=True,null=True)
    phone = models.CharField(max_length=30,blank=True,null=True)
    Tel   = models.CharField(max_length=30 ,blank=True,null=True)


    def __str__(self):
        return self.user.username


@receiver(user_signed_up)
def create_profile(sender, **kwargs):
    u = Profile.objects.create(user=kwargs['user'])
    u.save()