from django import template
from goods.models import Category

register = template.Library()


@register.inclusion_tag('cat_list.html')
def get_category_list():
    return {'cats': Category.objects.all()}