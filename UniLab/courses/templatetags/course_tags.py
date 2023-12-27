from django import template
from ..models import Course

register = template.Library()

@register.simple_tag
def get_courses_by_category(category_id):
    category_courses = Course.objects.filter(categories__id=category_id)
    return category_courses
