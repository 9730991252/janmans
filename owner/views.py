from django.shortcuts import redirect, render
from .models import *
# Create your views here.
def owner_home(request):
    if request.session.has_key('owner_mobile'):
        context={
            'login':1
        }
        return render(request, 'owner/owner_home.html',context)
    else:
        return redirect('/login/')
    
def add_category(request):
    if request.session.has_key('owner_mobile'):
        if 'add_category'in request.POST:
            name = request.POST.get('name').upper()
            if Category.objects.filter(name=name).exists():
                pass
            else:
                Category(
                    name = name,
                    status = 1
                ).save()
            return redirect('/owner/add_category/')
        if 'active'in request.POST:
            id = request.POST.get('id')
            c = Category.objects.filter(id=id).first()
            c.status = 0
            c.save()
            return redirect('/owner/add_category/')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            c = Category.objects.filter(id=id).first()
            c.status = 1
            c.save()
            return redirect('/owner/add_category/')
        if 'edit_category'in request.POST:
            id = request.POST.get('id')
            name = request.POST.get('name').upper()
            Category(
                id=id,
                name = name,
                status = 1
            ).save()
            return redirect('/owner/add_category/')
            
        context={
            'login':1,
            'category':Category.objects.all()
        }
        return render(request, 'owner/add_category.html',context)
    else:
        return redirect('/login/')
    
def add_blog(request):
    if request.session.has_key('owner_mobile'):
        if 'add_post'in request.POST:
            heading = request.POST.get('heading').upper()
            image = request.FILES.get('image')
            category_id = request.POST.get('category')
            description = request.POST.get('description')
            print(description)
            if Post.objects.filter(heading=heading).exists():
                pass
            else:
                Post(
                    heading = heading,
                    image = image,
                    category_id = category_id,
                    description = description,
                    status = 1
                ).save()
            return redirect('/owner/add_blog/')
        if 'active'in request.POST:
            id = request.POST.get('id')
            c = Post.objects.filter(id=id).first()
            c.status = 0
            c.save()
            return redirect('/owner/add_blog/')
        if 'deactive'in request.POST:
            id = request.POST.get('id')
            c = Post.objects.filter(id=id).first()
            c.status = 1
            c.save()
            return redirect('/owner/add_blog/')
        if 'edit_post'in request.POST:
            id = request.POST.get('id')
            heading = request.POST.get('heading').upper()
            image = request.FILES.get('image')
            c_id = request.POST.get('category')
            description = request.POST.get('description')
            c = Post.objects.filter(id=id).first()
            if image == None:
                image = c.image
            c.heading = heading
            c.image = image
            c.category_id = c_id
            c.description = description
            c.save()
            return redirect('/owner/add_blog/')
        context={
            'login':1,
            'post':Post.objects.all().order_by('-id'),
            'category':Category.objects.filter(status=1).order_by('-id'),
        }
        return render(request, 'owner/add_blog.html',context)
    else:
        return redirect('/login/')