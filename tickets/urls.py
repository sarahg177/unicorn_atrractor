from django.urls import path
from tickets import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('ticket_list', views.get_ticket_list, name='ticket_list'),
    path('single_view', views.view_ticket_details, name='single_view'),
    path('create_ticket', views.create_a_new_ticket, name='create_ticket'),
    path('upvote', views.vote_for_ticket, name='upvote'),
    path('edit', views.edit_a_bug, name='edit'),
    path('feature_payment', views.feature_payment, name='feature_payment'),
]
