from django.urls import path

from .import views

urlpatterns = [
    path('',views.home,name= "home"),
    path('posts/',views.posts_list,name= "posts_list"),
    path('posts/<slug>',views.posts_detail,name= "posts_detail"),
]
