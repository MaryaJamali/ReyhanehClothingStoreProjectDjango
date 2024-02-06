from django import template

register = template.Library()


# Writing a tag template to separate three by three prices
@register.filter(name='three_digits_currency')
def three_digits_currency(value: int):
    return '{:,}'.format(value) + ' تومان'


# Writing a tag template to multiply the price of a single product by its number
@register.simple_tag
def multiply(quantity, price, *args, **kwargs):
    return three_digits_currency(quantity * price)

