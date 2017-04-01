from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='times') 
def times(number):
    return range(number)

"Multiplies the arg and the value"
@register.filter(name='multiply')
def multiply(value, arg):
	return value * arg

@register.filter(name='multiply')
def add(value, arg):
	return int(value) + int(arg)

@register.filter(name='keyvalue')
def keyvalue(d, key):
	return d.get(key)

@register.filter(name='todate')
def todate(timestamp):
	return datetime.fromtimestamp(float(timestamp))
