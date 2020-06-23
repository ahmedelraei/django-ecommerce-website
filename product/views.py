import datetime
import random
import string

from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.utils import timezone
from django.views.generic import DetailView, ListView, View
from payment.models import Payment
from clients.models import Address, Profile

from .extras import *
from .forms import *
from .models import *
from django.utils import translation

def ref_code_generator():
    ref = ''.join(random.choices(string.ascii_lowercase + string.digits,k=20))
    print(ref)
    return ref

def home(request):
    products = Product.objects.all()
    cats = Category.objects.all()
    slider = MainSlider.objects.all()
    context = {'products':products,'cats':cats,'slider':slider}
    return render(request,'Product/index.html',context)

class cart(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):
        try:
            order = Order.objects.get(user=self.request.user,ordered=False)
            context = {'object':order}
            return render(self.request,'Product/cart.html', context)
        except ObjectDoesNotExist:
            return render(self.request,'Product/cart.html')


def product_details(request,slug):
    product_details = Product.objects.get(PRDslug=slug)
    PRDid = product_details.id
    images = ProductImage.objects.filter(PRD=PRDid)
    context = {'product':product_details,'images':images}
    return render(request,'Product/product.html',context)


class cat(ListView):
    model = Category
    template_name = 'Product/category.html'

    def get_queryset(self):
        kwargs = self.kwargs
        qs = kwargs.get('slug')
        category = Category.objects.get(CATslug=qs)
        cat_id = category.id
        if category.CATparent:
            raise Http404()
        else:
            subs = Category.objects.filter(CATparent=cat_id)
            vals = subs.values('id')
            ids = []
            for val in vals:
                id = val.get('id')
                ids.append(id)
            subcategory_filter = Product.objects.filter(PRDcategory_id__in=ids)
            query = Product.objects.filter(PRDcategory_id=cat_id) | subcategory_filter
            return query


class subCategory(ListView):
    model = Category
    template_name = 'Product/category.html'

    def get_queryset(self):
        kwargs = self.kwargs
        qs = kwargs.get('slug')
        category = Category.objects.get(CATslug=qs)
        cat_id = category.id
        if category.CATparent == None:
            raise Http404()
        else:
            return Product.objects.filter(PRDcategory=cat_id)

def search(request):
    try:
        query = request.GET.get('q')
    except:
        query = None
    if query:
        results = Product.objects.filter(
            Q(PRDname__icontains=query) | Q(PRDdesc__icontains=query)
            )
        """ results = Product.objects.annotate(
            search=SearchVector('PRDname','PRDdesc','PRDdetails')
        ).filter(search=query) """
        context = {'query':query,'results':results}
        template= 'Product/results.html'
        
    else:
        raise Http404()

    return render(request, template, context)

@login_required
def addToCart(request,slug):
    item = get_object_or_404(Product,PRDslug=slug)
    order_item,created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__PRDslug=item.PRDslug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request,"This Item Quantity was updated.")
            return redirect("products:product_details" ,slug=slug)
        else:
            order.items.add(order_item)
            messages.info(request,"This Item is Added to your cart.")
            return redirect("products:product_details" ,slug=slug)
    else:

        order = Order.objects.create(user=request.user,order_ref=ref_code_generator())
        order.items.add(order_item)
        messages.info(request,"This Item is Added to your cart.")
    return redirect("products:product_details" ,slug=slug)

@login_required
def increaseCart(request,slug):
    item = get_object_or_404(Product,PRDslug=slug)
    order_item,created = OrderItem.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
        )
    order_qs = Order.objects.filter(user=request.user, ordered=False)

    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__PRDslug=item.PRDslug).exists():
            order_item.quantity +=1
            order_item.save()
            messages.info(request,"This Item Quantity was updated.")
            return redirect("products:cart")
        else:
            order.items.add(order_item)
            messages.info(request,"This Item is Added to your cart.")
            return redirect("products:product_details" ,slug=slug)
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request,"This Item is Added to your cart.")
    return redirect("products:product_details" ,slug=slug)

@login_required
def removeFromCart(request,slug):
    item = get_object_or_404(Product,PRDslug=slug)

    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
        )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__PRDslug=item.PRDslug).exists():
            order_item = OrderItem.objects.filter(
            item=item,
            user=request.user,
            ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            messages.info(request,"This Item was removed from your cart.")
            return redirect("products:cart")
        else:
            messages.info(request,"This Item was not in your cart.")
            return redirect("products:product_details" ,slug=slug)
    else:
        messages.info(request,"Yoou do not have an active order.")
        return redirect("products:product_details" ,slug=slug)


@login_required
def decreaseFromCart(request,slug):
    item = get_object_or_404(Product,PRDslug=slug)

    order_qs = Order.objects.filter(
        user=request.user,
        ordered=False
        )
    if order_qs.exists():
        order = order_qs[0]
        if order.items.filter(item__PRDslug=item.PRDslug).exists():
            order_item = OrderItem.objects.filter(
            item=item,
            user=request.user,
            ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
                messages.info(request,"This Item quantity was decreased.")
            else:
                order.items.remove(order_item)
                order_item.delete()
            return redirect("products:cart")
        else:
            messages.info(request,"This Item was not in your cart.")
            return redirect("products:product_details" ,slug=slug)
    else:
        messages.info(request,"Yoou do not have an active order.")
        return redirect("products:product_details" ,slug=slug)

def is_valid_form(values):
    valid = True
    for field in values:
        print("FIELDS",field)
        if field == "":
            valid = False
    return valid

class checkout(LoginRequiredMixin,View):
    def get(self,*args,**kwargs):  
        form = CheckoutForm()
        try:
            order = get_object_or_404(Order,user=self.request.user,ordered=False)
            context = {
                'object':order,
                'form':form,
                }

            shipping_address_qs = Address.objects.filter(
                user=self.request.user,
                default=True
            )


            if shipping_address_qs.exists():
                context.update({'default_shipping_address':shipping_address_qs[0]})

            return render(self.request,"Product/checkout.html",context)
        except ObjectDoesNotExist:
            return reverse('products:checkout')

    def post(self,*args,**kwargs):
        form = CheckoutForm(self.request.POST or None)
        try:
            order = Order.objects.get(user=self.request.user,ordered=False)

            if form.is_valid():
                use_default_shipping = form.cleaned_data.get('use_default_shipping')
                if use_default_shipping:
                    print("using default shipping address")
                    address_qs = Address.objects.filter(
                        user=self.request.user,
                        default=True
                    )
                    if address_qs.exists():
                        shipping_address = address_qs[0]
                        order.shippingAddress = shipping_address
                        order.save()

                    else:
                        messages.info(self.request,'No Default Shipping Address')
                        return redirect('products:checkout')
                
                else:
                    print("user is entering new shipping address")
                    shipping_address = form.cleaned_data.get('shipping_address')
                    shipping_address2 = form.cleaned_data.get('shipping_address2')
                    shipping_zip = form.cleaned_data.get('shipping_zip')
                    shipping_country = form.cleaned_data.get('shipping_country')
                    shipping_city = form.cleaned_data.get('shipping_city')
                    
                    if is_valid_form([shipping_address,shipping_zip
                    ,shipping_country,shipping_city]):

                        address = Address(
                            user=self.request.user,
                            street_address=shipping_address,
                            address2=shipping_address2,
                            zipCode=shipping_zip,
                            country=shipping_country,
                            city=shipping_city
                            )
                        address.save()
                        order.shippingAddress = address
                        order.save()

                        set_default_shipping =  form.cleaned_data.get('set_default_shipping')
                        
                        if set_default_shipping:
                            address.default = True
                            address.save()
                    else:
                        messages.info(self.request,'Please fill in required shiping address fields')
                        return redirect('product:checkout')


                payment_option = form.cleaned_data.get('payment_option')
                if payment_option == 'C':
                    order = Order.objects.get(user=self.request.user,ordered=False)
                    order_items = OrderItem.objects.filter(user=self.request.user,ordered=False)
                    for item in order_items:
                        item.ordered = True
                        item.save()
                    payment = Payment(
                                user = self.request.user,
                                order_id = order.order_ref,
                                amount = order.getTotal(),
                                success = True,
                                timestamp = timezone.now(),
                                payment_type = payment_option,
                            )
                    payment.save()
                    order.payment = payment 
                    order.orderTotal = order.getTotal()
                    order.ordered_date = timezone.now()
                    order.ordered = True
                    order.processing = True
                    order.save()
                    for item in order_items:
                        print(item.item.stock_quantity,item.quantity)
                        item.item.stock_quantity -= item.quantity
                        item.item.save()
                    messages.success(self.request,'Your Order has processed Successfully')
                    return redirect('clients:profile')

                if payment_option == 'W':
                    return redirect('payment:e-wallet')
                else:
                    messages.warning(self.request,"Failed to Checkout")
                    return redirect('products:checkout')
            

        except ObjectDoesNotExist:
            return redirect("products:cart")
