from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .forms import eWalletForm
from product.models import Order,OrderItem
from django.views.generic import DetailView, ListView, View
from django.contrib import messages
from .models import Payment
from django.utils import timezone
from django.shortcuts import redirect


class PAY_eWallet(View):
	def get(self,*args,**kwargs):
		template_name = 'Payment/eWallet.html'
		form = eWalletForm(self.request.GET or None)
		context = {'form':form}
		return render(self.request,template_name,context)
    
	def post(self,*args, **kwargs):
		form = eWalletForm(self.request.POST or None)
		order = Order.objects.get(user=self.request.user,ordered=False)
		order_items = OrderItem.objects.filter(user=self.request.user,ordered=False)
		if form.is_valid():
			sender = form.cleaned_data.get('sender_number')
			for item in order_items:
				item.ordered = True
				item.save()
			payment = Payment(
						user = self.request.user,
						order_id = order.order_ref,
						sender = sender,
						amount = order.getTotal(),
						success = True,
						timestamp = timezone.now(),
						payment_type = 'W',
					)

			payment.save()

			order.orderTotal = order.getTotal()
			order.ordered_date = timezone.now()
			order.ordered = True
			order.save()
			messages.success(self.request,'Your Order has processed Successfully')
			return redirect('clients:profile')