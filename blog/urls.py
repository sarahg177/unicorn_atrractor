from django.urls import path
from blog import views

urlpatterns = [
    path('', views.get_posts, name='blog_list'),
    path('new_post', views.create_post, name='new_post')
]