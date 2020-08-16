from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import DetailView, ListView, View
from product.models import Order
from django.http import HttpResponseRedirect
from .forms import EditAddressForm, editProfile, trackOrderForm , CancelOrderForm
from .models import Address, Profile


class profile(View):
    def get(self,*args,**kwargs):
        form = editProfile(self.request.POST or None)
        profile = Profile.objects.get(user=self.request.user)
        orders = Order.objects.filter(user=self.request.user).order_by('-ordered_date')
        context = {
            'form':form,
            'user':self.request.user,
            'profile':profile,
            'orders':orders,
            }
        return render(self.request,'profile.html',context)
    def post(self,*args,**kwargs):
        form = editProfile(self.request.POST or None)
        profile =  Profile.objects.filter(user=self.request.user)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            firstname = form.cleaned_data.get('firstname')
            lastname = form.cleaned_data.get('lastname')
            email = form.cleaned_data.get('email')
            phone = form.cleaned_data.get('phone')
            pic = form.cleaned_data.get('pic')

            profile.update(
                firstname=firstname,
                lastname=lastname,
                email=email,
                phone=phone,
                picture=pic.url
            )
            print("POST successful")
            return redirect("clients:profile")

class trackOrderView(LoginRequiredMixin,View):
    def get(self,*args, **kwargs):
        ''' form = trackOrderForm(self.request.GET or None)
        context = {'form':form} '''
        return render(self.request,'track_order.html',{})

''' @login_required
def trackOrder(request):
    try:
        query = request.GET.get('order_ref').strip()
    except:
        query = None
    order_qs =  Order.objects.filter(user=request.user,order_ref=query)
    if order_qs.exists():
        context = {'order':order_qs[0]}
        return render(request,'track_result.html',context)
    else:
        messages.info(request,"No such Order")
        return redirect("clients:track-order")
 '''

def is_valid_form(values):
    valid = True
    for field in values:
        if field == "":
            valid = False
    return valid

    
class EditAddress(View):
    def get(self,*args, **kwargs):
        form = EditAddressForm(self.request.GET or None)
        address = Address.objects.get(user=self.request.user,pk=self.kwargs['pk'])
        profile = Profile.objects.get(user=self.request.user)
        context = {'form':form,'address':address,'profile':profile}
        return render(self.request,'edit_address.html',context)
    
    def post(self,*args, **kwargs):
        form = EditAddressForm(self.request.POST or None)
        try:
            address = Address.objects.filter(user=self.request.user,pk=self.kwargs['pk'])
            if form.is_valid():
                street_address = form.cleaned_data.get('street_address')
                address2 = form.cleaned_data.get('address2')
                zipCode = form.cleaned_data.get('zipCode')
                city = form.cleaned_data.get('city')
                default = form.cleaned_data.get('default')

                if is_valid_form([street_address,address2,zipCode,city]):

                    address.update(
                        user=self.request.user,
                        street_address=street_address,
                        address2=address2,
                        zipCode=zipCode,
                        city=city,
                        default=default,
                    )

                    messages.success(self.request,'Your Address has been updated successfully')
                    return redirect('clients:profile')

                else:
                    messages.info(self.request,'Please fill in required address fields')
            
            else:
                messages.info(self.request,'error')
                return redirect('clients:profile')
                
        except ObjectDoesNotExist:
            messages.info(self.request,'no such address')
            

class CancelOrder(View):

    def get(self,*args, **kwargs):
        form = CancelOrderForm(self.request.GET or None)
        context = {'form':form}
        return render(self.request,'cancel-order.html',context)

    def post(self,*args, **kwargs):
        try:
            form = CancelOrderForm(self.request.POST or None)
            order_ref = self.kwargs['code']

            order = Order.objects.get(user=self.request.user,order_ref=order_ref,cancelled=False)
            if order.delivered == False and order.shipped == False:
                order.cancelled = True
                order.save()
                
                messages.success(self.request,'order has been cancelled')
                return redirect('clients:profile')

            elif order.shipped == True:
                messages.success(self.request,'order has been already shipped')
                return redirect('clients:profile')
            else:
                messages.success(self.request,'order has been already delivered')
                return redirect('clients:profile')

        except ObjectDoesNotExist:
            messages.info(self.request,'no such order')
            return redirect('clients:track-order')

def SelectCurrency(request):
    last_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        request.session['currency'] = request.POST['currency']
    
    return HttpResponseRedirect(last_url)