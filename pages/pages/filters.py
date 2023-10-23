from django import template

register = template.Library()

@register.filter(name='capitalize_words')
def capitalize_words(value):
    words = value.split()
    return ' '.join([word.capitalize() for word in words])
