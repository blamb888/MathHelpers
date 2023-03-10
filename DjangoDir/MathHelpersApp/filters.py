import base64

from django import template
from django.utils.encoding import force_bytes

register = template.Library()

@register.filter
def base64_encode(value):
    """
    Base64 encode the input value.
    """
    if value is None:
        return ''
    return base64.b64encode(force_bytes(value)).decode('utf-8')
