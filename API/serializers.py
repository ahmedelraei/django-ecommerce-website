from product.models import Product , Category , Order
from clients.models import Address
from rest_framework import serializers
import datetime
from currencies.models import Currency


class ProductSerializer(serializers.ModelSerializer):
    PRDcategory = serializers.StringRelatedField()
    PRDshipping_regions = serializers.SerializerMethodField()
    PRDprice = serializers.SerializerMethodField()
    PRDbrand = serializers.StringRelatedField()
    url = serializers.CharField(source='get_absolute_url')
    img = serializers.CharField(source='GetMainimg')
    class Meta:
        model = Product
        fields = (
                'PRDname',
                'PRDcategory',
                'PRDbrand',
                'PRDdesc',
                'PRDdetails',
                'PRDshipping_notes',
                'PRDshipping_regions',
                'PRDimage',
                'PRDprice',
                'PRDdiscount',
                'stock_quantity',
                'PRDcreated',
                'PRDslug',
                'PRDisNew',
                'PRDisTrend',
                'url',
                'img',
        )
    def get_PRDshipping_regions(self,obj):
        return obj.get_shipping_regions()
    
    def get_PRDprice(self,obj):
        price = obj.PRDprice
        currency = Currency.objects.all()
        request = self.context.get('request')
        if request.session['currency'] == 'EGP':
           price = obj.PRDprice * currency[0].factor
        return price

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")

class OrderSerializer(serializers.ModelSerializer):
    total = serializers.SerializerMethodField()
    state = serializers.CharField(source='getState')
    cancel_url = serializers.CharField(source='get_cancel_url')
    items = serializers.SerializerMethodField()
    listed_date = serializers.CharField()
    ordered_date = serializers.CharField()
    shippingAddress = serializers.SerializerMethodField()
    class Meta:
        model = Order
        fields = ('__all__')
    
    def get_items(self,obj):
        items = []
        item = []
        for orderitem in obj.items.all():
            items.append(orderitem.__str__() + ' of id = ' + str(orderitem.item.pk))
        return items

    def get_total(self,obj):
        total = obj.getTotal()
        currency = Currency.objects.all()
        request = self.context.get('request')
        if request.session['currency'] == 'EGP':
           total = total * currency[0].factor
        return total
    
    def get_shippingAddress(self,obj):
        address = {
            'street_address':obj.shippingAddress.street_address,
            'address2':obj.shippingAddress.address2,
            'zipCode':obj.shippingAddress.zipCode,
            'country':obj.shippingAddress.country.name,
            'city':obj.shippingAddress.city,
            'default':obj.shippingAddress.default,
        }
        return address
    
