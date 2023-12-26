from decimal import Decimal
from django import template

register = template.Library()

@register.filter
def calc_discount(price, discount_percent):
    if isinstance(price, Decimal):
        price = float(price)
    discount_amount = price * (discount_percent / 100)
    discounted_price = price - discount_amount
    return Decimal(str(discounted_price))