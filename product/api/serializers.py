from rest_framework import serializers
from product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'PRDname',
            'PRDcategory',
            'PRDbrand',
            'PRDdesc',
            'PRDdetails',
            'PRDshipping_notes',
            #TODO:'PRDshipping_regions',
            'PRDimage',
            'PRDprice',
            'PRDdiscount',
            'PRDcost',
            'stock_quantity',
            'PRDcreated',
            'PRDslug',
            'PRDisNew',
            'PRDisTrend',
        )