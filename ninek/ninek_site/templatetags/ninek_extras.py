from django import template
from ninek_site.models import Category

register = template.Library()

@register.inclusion_tag('ninek_site/category_list.html')
def get_category_list():
    category = Category.objects.all()[:5]
    return {'category': category}