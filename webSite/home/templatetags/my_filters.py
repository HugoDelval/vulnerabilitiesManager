from django import template

register = template.Library()


@register.filter(name='times')
def times(number):
    try:
        a = range(number+1)
    except TypeError:
        a = range(1)
    return a


@register.filter
def keyvalue(dict, key):
    return dict[key]


@register.filter
def addstr(arg1, arg2):
    """concatenate arg1 & arg2"""
    return str(arg1) + str(arg2)