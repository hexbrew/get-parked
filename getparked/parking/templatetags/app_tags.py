from django import template
register = template.Library()


@register.simple_tag
def is_bay_occupied(bay, day):
    return bay.is_occupied(day)
    
@register.simple_tag
def get_bay_booking(bay, day):
    return bay.get_day_booking(day)