# custom tags stay in here
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

#Function that takes a text and turns it into the same text but in another color.
@register.filter
def ExampleCustom_filter(text, color):
    safe_text = '<span style="color:{color}">{text}</span>'.format(color=color, text=text)
    return mark_safe(safe_text)


#Function that returns a icon depending on the area_code.
@register.filter(is_safe=True)
def area_icon(area_code, chosen_area):
    if area_code == 'DEV' and chosen_area == 'DEV':
        safe_text = '<i class="bi bi-code-slash icon bg-primary text-white rounded-circle p-3"></i>'
        return  mark_safe(safe_text)  
    elif area_code == 'DEV':
        safe_text = '<i class="bi bi-code-slash icon bg-secondary text-white rounded-circle p-3"></i>'
        return  mark_safe(safe_text) 

    elif area_code == 'SUP' and chosen_area == 'SUP':
        safe_text = '<i class="bi bi-headset icon bg-primary text-white rounded-circle p-3"></i>'
        return mark_safe(safe_text)
    elif area_code == 'SUP':
        safe_text = '<i class="bi bi-headset icon bg-secondary text-white rounded-circle p-3"></i>'
        return mark_safe(safe_text)

    elif area_code == 'INF' and chosen_area == 'INF':
        safe_text = '<i class="bi bi-server icon bg-primary text-white rounded-circle p-3"></i>'
        return mark_safe(safe_text)
    elif area_code == 'INF':
        safe_text = '<i class="bi bi-server icon bg-secondary text-white rounded-circle p-3"></i>'
        return mark_safe(safe_text)

    elif area_code == 'CIE' and chosen_area == 'CIE':
        safe_text = '<i class="bi bi-pie-chart icon bg-primary text-white rounded-circle p-3"></i>'
        return mark_safe(safe_text)
    elif area_code == 'CIE':
        safe_text = '<i class="bi bi-pie-chart icon bg-secondary text-white rounded-circle p-3"></i>'
        return mark_safe(safe_text)

    elif area_code == 'SEG' and chosen_area == 'SEG':
        safe_text = '<i class="bi bi-shield-shaded icon bg-primary text-white rounded-circle p-3"></i>'
        return mark_safe(safe_text)
    elif area_code == 'SEG':
        safe_text = '<i class="bi bi-shield-shaded icon bg-secondary text-white rounded-circle p-3"></i>'
        return mark_safe(safe_text)

    elif area_code == 'PRO' and chosen_area == 'PRO':
        safe_text = '<i class="bi bi-box-seam icon bg-primary text-white rounded-circle p-3"></i>'
        return mark_safe(safe_text)
    elif area_code == 'PRO':
        safe_text = '<i class="bi bi-box-seam icon bg-secondary text-white rounded-circle p-3"></i>'
        return mark_safe(safe_text)

    else:
        safe_text = '<i class="bi bi-bug icon bg-primary text-white rounded-circle p-3"></i>'
        return mark_safe(safe_text)
    
    
