# custom tags stay in here
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def ExampleCustom_filter(text):
    if text == 'Desenvolvimento':
        safe_text = '<span style="color:{color}">{text}</span>'.format(color='red', text=text)
        return mark_safe(safe_text)
    if text == 'Suporte':
        safe_text = '<span style="color:{color}">{text}</span>'.format(color='orange', text=text)
        return mark_safe(safe_text)
    if text == 'Infraestrutura':
        safe_text = '<span style="color:{color}">{text}</span>'.format(color='blue', text=text)
        return mark_safe(safe_text)
    if text == 'Ciência de Dados':
        safe_text = '<span style="color:{color}">{text}</span>'.format(color='purple', text=text)
        return mark_safe(safe_text)
    if text == 'Segurança':
        safe_text = '<span style="color:{color}">{text}</span>'.format(color='green', text=text)
        return mark_safe(safe_text)
    if text == 'Produto':
        safe_text = '<span style="color:{color}">{text}</span>'.format(color='black', text=text)
        return mark_safe(safe_text)
    else:
        return text

@register.filter
def Area_filter(areaCode):

    #return 
    "grey out all other area icons except the one that was clicked on"