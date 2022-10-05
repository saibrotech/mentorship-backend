# custom tags stay in here
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

AREA_ICONS = {
    'DEV': 'bi-code-slash',
    'SUP': 'bi-headset',
    'INF': 'bi-server',
    'CIE': 'bi-pie-chart',
    'SEG': 'bi-shield-shaded',
    'PRO': 'bi-box-seam'
}

#Function that returns a icon depending on the area_code.
@register.filter(is_safe=True)
def area_icon(area_code, chosen_area):
    if area_code == chosen_area:
        background = 'bg-primary'
    else:
        background = 'bg-secondary'

    class_icon = AREA_ICONS[area_code] if AREA_ICONS[area_code] else 'bi-bug'
    safe_text = f'<i class="bi {class_icon} icon {background} text-white rounded-circle p-3"></i>'
    return mark_safe(safe_text)
