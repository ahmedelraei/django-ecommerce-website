from django.db import models
from django.conf import settings

PAY_CHOICES = (
    #('S','Card'),
    #('P','Paypal'),
    ('C','Cash'),
    ('F','Fawry'),
    ('W','e-Wallet'),

)
class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL
    ,on_delete=models.CASCADE, blank=True,null=True)
    token = models.CharField(max_length=50,blank=True, null=True)
    order_id = models.CharField(max_length=120)
    sender = models.CharField(max_length=11,blank=True, null=True)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    success = models.BooleanField(default=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    payment_type = models.CharField(max_length=1,choices=PAY_CHOICES)
    
    def __str__(self):
        return self.user.username
    
