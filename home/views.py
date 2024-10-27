from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages 
from owner.models import *
# Create your views here.
def index(request):
    ip = user_ip(request)
    context={
        'ip':ip,
        'post':Post.objects.filter(status=1).order_by('-id'),
        'category':Category.objects.filter(status=1),
    }
    return render(request, 'home/index.html',context)

def user_like_post(request):
    if request.method == 'GET':
        id = request.GET['id']
        ip = request.GET['ip']
        user = User.objects.filter(user = ip).first()
        if Post_like.objects.filter(post_id=id, user_id=user.id, status=1).exists():
            p = Post_like.objects.filter(post_id=id, user__user=ip).first()
            p.status = 0
            p.save()
            post_like = Post_like.objects.filter(post_id=id, status = 1).count()
            t = '<i class="fa-regular fa-thumbs-up"></i>&nbsp;'+ str(post_like) +'+'
        elif Post_like.objects.filter(post_id=id, user_id=user.id, status=0).exists():
            p = Post_like.objects.filter(post_id=id, user__user=ip).first()
            p.status = 1
            p.save()
            post_like = Post_like.objects.filter(post_id=id, status = 1).count()
            t = '<i class="fa-solid fa-thumbs-up"></i>&nbsp;'+ str(post_like) +'+'
        else:
            Post_like(
                post_id=id,
                user_id=user.id
            ).save()
            post_like = Post_like.objects.filter(post_id=id, status = 1).count()
            t = '<i class="fa-solid fa-thumbs-up"></i>&nbsp;'+ str(post_like) +'+'
    return JsonResponse({'t':t})
    

def user_ip(request):
    adress = request.META.get('HTTP_X_FORWARDED_FOR')
    if adress:
        ip = adress.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    if User.objects.filter(user=ip).exists():
        return ip
    else:
        User(user=ip).save()
        return ip

def post_detail(request, id):
    ip = user_ip(request)
    views = post_views_count(id)
    c = Post.objects.filter(id=id).first()
    user = User.objects.filter(user=ip).first()
    if Post_like.objects.filter(user_id=user.id).exists():
        user_like = 'yes'
    else:
        user_like = ''
    context={
        'user_like':user_like,
        'ip':ip,
        'post':Post.objects.filter(status=1, id=id).first(),
        'all_post':Post.objects.filter(status=1, category_id=c.category_id).order_by('-id'),
        'category':Category.objects.filter(status=1),
        'views':views
    }
    return render(request, 'home/post_detail.html',context)

def post_views_count(id):
    if Post_views.objects.filter(post_id=id).exists():
        p = Post_views.objects.filter(post_id=id).first()
        p.count += 1
        p.save()
    else:
        Post_views(
            post_id = id,
            count = 1
        ).save()
    p = Post_views.objects.filter(post_id=id).first()
    return p.count

def category_detail(request, id):
    ip = user_ip(request)
    context={
        'ip':ip,
        'category':Category.objects.filter(id=id).first(),
        'post':Post.objects.filter(status=1, category_id=id),
        'all_category':Category.objects.filter(status=1),
    }
    return render(request, 'home/category_detail.html',context)






def login(request):
    if request.session.has_key('owner_mobile'):
        return redirect('/owner/owner_home/')
    if 'Login' in request.POST:
        num = request.POST.get('number')
        pin = request.POST.get('pin')
        owner_login={'mobile':'1252','pin':'1252'}
        if owner_login["mobile"]==num and owner_login["pin"]==pin:
            request.session['owner_mobile'] = request.POST.get('number')
            return redirect('/owner/owner_home/')
        else:
            messages.warning(request,"please insert correct information or call more suport 9730991252")
    return render(request, 'home/login.html')