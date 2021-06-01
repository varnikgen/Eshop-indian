from django import template


register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "₽ " + str(number)

@register.filter(name='multiplay')
def multiplay(qnt, price):
    return qnt * price
