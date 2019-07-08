from django.shortcuts import render
from tickets.models import Ticket


def welcome(request):
    return render(request, 'welcome_page.html')


def get_ticket_list(request):
    """Shows list of all tickets"""
    bugs = Ticket.objects.all(
    )

    return render(request, "view_ticket_list.html", {'bugs': bugs})
