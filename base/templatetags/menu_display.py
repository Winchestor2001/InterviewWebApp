from django import template
from base.models import MenuItem

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context['request']
    current_path = str(request.path).split('/')[-2]
    menu_items = MenuItem.objects.filter(menu_name=menu_name).select_related('parent')
    menu_html = '<ul class="menu">'
    for menu_item in menu_items:

        if not menu_item.parent:
            menu_html += '<li class="top-menu-item">'
        else:
            menu_html += '<li>'


        if current_path.replace('/', '') == menu_item.url:
            active_class = 'active'
        else:
            active_class = ''

        menu_html += '<a href="/menu/{0}" class="{1}">{2}</a>'.format(menu_item.url, active_class, menu_item.title)
        
        if menu_item.children.all():
            menu_html += draw_sub_menu(menu_item, current_path)

        menu_html += '</li>'
    menu_html += '</ul>'

    return menu_html


def draw_sub_menu(menu_item, current_path):
    sub_menu_html = '<ul class="sub-menu">'
    for child in menu_item.children.all():
        if current_path.startswith(child.url):
            active_class = 'active'
        else:
            active_class = ''
        sub_menu_html += '<li><a href="/menu/{0}" class="{1}">{2}</a>'.format(child.url, active_class, child.title)
        if child.children.all():
            sub_menu_html += draw_sub_menu(child, current_path)
        sub_menu_html += '</li>'
    sub_menu_html += '</ul>'
    return sub_menu_html
