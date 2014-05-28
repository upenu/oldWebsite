from django import template
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