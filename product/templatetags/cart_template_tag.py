from django import template
from product.models import OrderItem

register = template.Library()

@register.filter
def cartItemCount(user):
    if user.is_authenticated:
        qs = OrderItem.objects.filter(user=user, ordered=False)
        if qs.exists():
            count = 0
            for item in qs:
                print(item)
                count += int(str(item).split()[0])
            return count
    return 0
