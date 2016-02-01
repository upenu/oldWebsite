from django.template import Library

register = Library()

@register.filter(name='cut')
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return str(value).replace(arg, '')