from django import template
from owner.models import *
from datetime import timedelta, date
register = template.Library()

@register.simple_tag
def post_views(id):
    count = Post_views.objects.filter(post_id=id).first()
    if count != None:
        return count.count
    else:
        return 0
    
from django.utils.safestring import mark_safe
@register.simple_tag
def user_like(id, ip):
    count = Post_like.objects.filter(post_id=id, status = 1).count()
    if Post_like.objects.filter(post_id=id, user__user=ip, status = 1).exists():
        t = ('<i class="fa-solid fa-thumbs-up"></i>&nbsp;'+ str(count) +'+')
    else:
        t = ('<i class="fa-regular fa-thumbs-up"></i>&nbsp;'+ str(count) +'+')
    return mark_safe(t)
