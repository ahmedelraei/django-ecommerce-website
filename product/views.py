from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render,redirect, get_object_or_404
from django.views.generic import ListView , DetailView ,View
from .models import *
from django.core.paginator import Paginator
from django.http import Http404 , HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone


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
        messages.error(self.request,"You do not have an active order")
        return redirect('/')

def allproducts(request):
    products = Product.objects.all()
    #paginator = Paginator(products,10)
    #page = request.GET.get('page')
    #products = paginator.get_page(page)
    context = {'products':products}
    return render(request,'Product/products.html',context)

class product_list(ListView):
    model = Product
    template_name = "Product/products.html"

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
        ordered_date = timezone.now()
        order = Order.objects.create(user=request.user,ordered_date=ordered_date)
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
    