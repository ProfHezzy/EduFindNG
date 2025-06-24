from django import template
register = template.Library()

@register.filter
def review_count(school):
    return school.reviews.count()
