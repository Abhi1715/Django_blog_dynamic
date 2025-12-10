from django.urls import path,include
from . views import posts_by_category
from . import views

urlpatterns = [
    path('<int:category_id>/',views.posts_by_category,name='posts_by_category')
]

