from django.urls import path
from tickets import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('ticket_list', views.get_ticket_list, name='ticket_list'),
]
