from django import template
import mimetypes

register = template.Library()

@register.filter
def is_image(file_url):
    mime = mimetypes.guess_type(file_url)[0]
    return mime and mime.startswith('image')
