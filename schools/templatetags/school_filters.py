from django import template
register = template.Library()

@register.filter
def format_fee(value):
    return f"₦{value:,}" if value else "N/A"
