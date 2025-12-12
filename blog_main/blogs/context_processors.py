from assignments.models import Sociallinks
from . models  import Category

def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_sociallinks(request):
    sociallinks = Sociallinks.objects.all()
    return dict(sociallinks=sociallinks)
    