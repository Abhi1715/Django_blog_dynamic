from django.shortcuts import render
from assignments.models import About
from blogs.models import Category,Blog

def home(request):
    
    featured = Blog.objects.filter(is_featured=True,status=1).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False ,status=1)
    try:
        about = About.objects.get()
    except:
        about=None
    context={
        
        'featured':featured,
        'posts' : posts,
        'about':about,
    }
    return render(request,'home.html',context)