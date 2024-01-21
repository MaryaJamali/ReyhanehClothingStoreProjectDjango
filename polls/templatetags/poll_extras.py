from django import template

register = template.Library()


# Writing a tag template to separate three by three prices
@register.filter(name='three_digits_currency')
def three_digits_currency(value: int):
    return '{:,}'.format(value) + ' تومان'

