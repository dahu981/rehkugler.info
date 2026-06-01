import re
from django import template
from django.conf import settings

register = template.Library()


@register.simple_tag
def strip_lang_prefix(path):
    lang_codes = [code for code, _ in settings.LANGUAGES]
    pattern = r'^/(' + '|'.join(lang_codes) + ')/'
    return re.sub(pattern, '/', path)
