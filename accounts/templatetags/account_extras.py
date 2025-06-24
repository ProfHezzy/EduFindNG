from django import template
register = template.Library()

@register.filter
def user_type_display(user):
    return user.get_user_type_display() if hasattr(user, 'get_user_type_display') else ''
