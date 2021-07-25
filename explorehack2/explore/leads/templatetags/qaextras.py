from django import template

register = template.Library()


def islist(value):
    return type(value) == type([])
register.filter('islist', islist)