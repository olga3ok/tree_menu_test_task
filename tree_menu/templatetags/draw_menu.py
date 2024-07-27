from django import template
from tree_menu.models import MenuItem, Menu

register = template.Library()


@register.inclusion_tag('menu.html')
def draw_menu(menu_name, sel_item=None, items=None, parent=None):

    if items is None:
        items = MenuItem.objects.select_related('parent', 'menu').filter(menu__name=menu_name)

    if sel_item and items is None and sel_item.menu.name != menu_name:
        sel_item = None

    context = {
        'menu': menu_name,
        'sel_item': sel_item,
        'items': items,
        'parent': parent,
    }

    return context
