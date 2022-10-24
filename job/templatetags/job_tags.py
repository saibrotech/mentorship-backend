# custom tags stay in here
from re import I
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

ICON_DICT = {
    'DEV': 'bi-code-slash',
    'SUP': 'bi-headset',
    'INF': 'bi-server',
    'CIE': 'bi-pie-chart',
    'SEG': 'bi-shield-shaded',
    'PRO': 'bi-box-seam'
}

# Function that returns a icon for the area depending on the area_code.

@register.filter(is_safe=True)
def area_icon(area_code, chosen_area):
    if area_code == chosen_area:
        background = 'bg-primary'
    else:
        background = 'bg-secondary'
    if area_code in ICON_DICT:
        class_icon = ICON_DICT[area_code] if ICON_DICT[area_code] else 'bi-bug'
        safe_text = f'<i class="bi {class_icon} icon {background} text-white rounded-circle"></i>'
        return mark_safe(safe_text)
    else:
        print("The category " + area_code + " doesn't exist.");
        safe_text = f'<i class="bi bi-bug icon {background} text-white rounded-circle"></i>'
        return mark_safe(safe_text)
