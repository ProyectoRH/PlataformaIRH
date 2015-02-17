from django import template

register = template.Library()

@register.filter(name='count_for')
def count_for(value):
	value = int(value) + 1
	return value