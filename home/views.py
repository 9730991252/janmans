from django.shortcuts import redirect, render
from django.contrib import messages 
from owner.models import *
# Create your views here.
def index(request):
    context={
        'post':Post.objects.filter(status=1),
        'category':Category.objects.filter(status=1),
        'last_post':Post.objects.filter(status=1).last()
    }
    return render(request, 'home/index.html',context)

def post_detail(request, id):
    c = Post.objects.filter(id=id).first()
    
    context={
        'post':Post.objects.filter(status=1, id=id).first(),
        'all_post':Post.objects.filter(status=1, category_id=c.category_id).order_by('-id'),
        'category':Category.objects.filter(status=1),
    }
    return render(request, 'home/post_detail.html',context)

def category_detail(request, id):
    context={
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