"""Tags used in template for job App."""

import logging
import types

from django import template
from django.utils.html import format_html

logger = logging.getLogger(__name__)
register = template.Library()

ICON_DICT = types.MappingProxyType({
    'DEV': 'bi-code-slash',
    'SUP': 'bi-headset',
    'INF': 'bi-server',
    'CIE': 'bi-pie-chart',
    'SEG': 'bi-shield-shaded',
    'PRO': 'bi-box-seam',
})


@register.filter(is_safe=True)
def area_icon(area_code, chosen_area):
    """
    Return an icon for the area depending on the area_code.

    Args:
        area_code (ICON_DICT): Area code for the icon
        chosen_area (str): Area code selected

    Returns:
        HTML for area icon
    """
    if area_code == chosen_area:
        background = 'bg-primary'
    else:
        background = 'bg-secondary'

    if area_code in ICON_DICT:
        class_icon = ICON_DICT.get(area_code)
    else:
        logger.warning("The category {0} doesn't exist.".format(area_code))
        class_icon = 'bi-bug'

    return format_html(
        '<i class="bi {0} icon {1} text-white rounded-circle"></i>',
        class_icon,
        background,
    )
