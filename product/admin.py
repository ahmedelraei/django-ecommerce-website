# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from clients.models import Address

class inlineAccessories(admin.StackedInline):
    model = Product_Accessories

class ProductAdmin(ImportExportModelAdmin):
    inlines = [inlineAccessories]
    list_display = ('PRDname','PRDcategory','PRDbrand','PRDprice','PRDdiscount','PRDslug')
    list_display_links = ('PRDname',)
    list_editable = ('PRDprice','PRDdiscount','PRDslug')
    list_filter = ('PRDcategory','PRDbrand')
    search_fields = ('PRDname','PRDslug')
    


admin.site.register(Product,ProductAdmin)

@admin.register(Category)
class CategoryExportImport(ImportExportModelAdmin):
    pass

@admin.register(ProductImage)
class ProductImageExportImport(ImportExportModelAdmin):
    pass

@admin.register(Product_Alternatives)
class Product_AltExportImport(ImportExportModelAdmin):
    pass

@admin.register(Product_Accessories)
class Product_AccessoriesExportImport(ImportExportModelAdmin):
    pass

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('user','item','quantity','ordered')
    list_display_links = ('user',)
    list_editable = ('item','quantity')
    list_filter = ('quantity','item','user')
    search_fields = ('user__username','item','quantity',)


class inlineAddresses(admin.StackedInline):
    model = Address
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'ordered_date',
        'order_ref',
        'orderTotal',
        'listed_date',
        'paid',
        'ordered',
        'processing',
        'cancelled',
        'shipped',
        'delivered',
        )
    list_display_links = ('user',)
    list_filter = ('ordered_date','ordered','listed_date','paid','orderTotal')
    search_fields = ('user__username','order_ref')


admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(MainSlider)

