from django.conf import settings
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

from product.models import Order,OrderItem

# Create your views here.


@csrf_exempt
def payment_done(request):
    order = get_object_or_404(Order, ordered=False)
    order.ordered = True
    order.save()
    order_item = get_object_or_404(OrderItem,user=request.user, ordered=False)
    order_item.ordered = True
    order_item.save()
    return render(request,'Payment/success.html')

@csrf_exempt
def payment_canceled(request):
	return render(request,'Payment/failed.html')



def payment_process(request):
	order = get_object_or_404(Order, ordered=False)
	host = request.get_host()

	paypal_dict = {
		'business':settings.PAYPAL_RECEIVER_EMAIL,
		'amount': '%.2f' % order.getTotal(),
		'item_name': 'Order {}'.format(order.id),
		'invoice': str(order.id),
		'currency_code':'USD',
		'notify_url': 'http://{}{}'.format(host,reverse('paypal-ipn')),
		'return_url': 'http://{}{}'.format(host,reverse('payment:success')),
		'cancel_return': 'http://{}{}'.format(host,reverse('payment:failed')),
	}
	form = PayPalPaymentsForm(initial=paypal_dict)
	context = {
	'order':order,
	'form':form,
	}
	return render(request,'Payment/process.html',context)
