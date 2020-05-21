from product.models import Product , Category
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    PRDcategory = serializers.StringRelatedField()
    PRDshipping_regions = serializers.SerializerMethodField()
    PRDbrand = serializers.StringRelatedField()
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
                'PRDcost',
                'stock_quantity',
                'PRDcreated',
                'PRDslug',
                'PRDisNew',
                'PRDisTrend',
        )
    def get_PRDshipping_regions(self,obj):
        return obj.get_shipping_regions()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("__all__")
