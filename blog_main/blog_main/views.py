from django.shortcuts import render
from blogs.models import Category,Blog

def home(request):
    
    featured = Blog.objects.filter(is_featured=True,status=1).order_by('updated_at')
    posts = Blog.objects.filter(is_featured=False ,status=1)
    context={
        
        'featured':featured,
        'posts' : posts,
    }
    return render(request,'home.html',context)