from django.urls import path
from blog import views

urlpatterns = [
    path('', views.get_posts, name='blog_list'),
    path('new_post', views.create_post, name='new_post'),
    path('edit_post', views.edit_a_blog, name='edit_post'),
    path('delete_post', views.delete_blog, name='delete_post'),
]