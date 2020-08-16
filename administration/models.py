from django.db import models
from django.conf import settings

class Logo(models.Model):
    logo = models.ImageField()

    class Meta:
        verbose_name_plural = "Logo"

    def get_absolute_image_url(self):
        return(self.logo.url)
