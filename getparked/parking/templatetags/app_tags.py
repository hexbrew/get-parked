from django import template
register = template.Library()


@register.simple_tag
def is_bay_occupied(bay, day):
    return bay.is_occupied(day)
