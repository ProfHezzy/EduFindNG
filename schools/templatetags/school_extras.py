from django import template
register = template.Library()

@register.filter
def school_type_display(profile):
    return profile.school_type
