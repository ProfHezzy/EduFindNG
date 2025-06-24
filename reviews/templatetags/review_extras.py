from django import template
register = template.Library()

@register.filter
def star_rating(value):
    return '★' * int(value) + '☆' * (5 - int(value))
