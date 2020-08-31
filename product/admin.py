# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from clients.models import Address

class inlineAccessories(admin.StackedInline):
    model = Product_Accessories
    extra = 1

class InlineProductImage(admin.StackedInline):
    model = ProductImage
    extra = 1

class ProductAdmin(ImportExportModelAdmin):
    inlines = [inlineAccessories,InlineProductImage]
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
    change_list_template = 'Product/orders_change_list.html'
    title = 'Hello'
    list_display = (
        'user',
        'ordered_date',
        'order_ref',
        'orderTotal',
        'listed_date',
        'get_payment_option',
        'ordered',
        'pending',
        'processing',
        'cancelled',
        'shipped',
        'delivered',
        #'testHtml',
        )
    def get_payment_option(self,obj):
        try:
            return obj.payment.payment_type
        except Exception as e: 
            print(e)

    get_payment_option.short_description  = 'Payment Type'
    list_display_links = ('user',)
    list_filter = ('ordered_date','ordered','listed_date','orderTotal','payment__payment_type')
    search_fields = ('user__username','order_ref')
    class Media:
        js = ('site_static/js/Chart.min.js','site_static/js/jquery-3.4.1.min.js')

    def changelist_view(self, request, extra_context=None):
        extra_context = {'onsale':['Item 1','Item 2']}
        return super(OrderAdmin, self).changelist_view(
            request, extra_context=extra_context
        )


class ItemVariationAdmin(admin.ModelAdmin):
    list_display = (
        'variation',
        'value',
        'image',
    )   
    list_filter = ('variation','variation__item')
    search_fields = ['value']

class ItemVariationInlineAdmin(admin.TabularInline):
    model = ItemVariation
    extra = 1

class VariationAdmin(admin.ModelAdmin):
    list_display = (
        'item',
        'name',
    )   
    list_filter = ('item',)
    search_fields = ['name']
    inlines = [ItemVariationInlineAdmin]

admin.site.register(OrderItem,OrderItemAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(MainSlider)
admin.site.register(ItemVariation,ItemVariationAdmin)
admin.site.register(Variation,VariationAdmin)

