from django.shortcuts import render
from django.utils import timezone
from tickets.models import Ticket


def welcome(request):
    return render(request, 'welcome_page.html')


def get_ticket_list(request):
    """Shows list of all tickets"""
    bugs = Ticket.objects.filter(
        created_date__lte=timezone.now(),
        issue_type=Ticket.Bug
    )
    features = Ticket.objects.filter(
        created_date__lte=timezone.now(),
        issue_type=Ticket.Feature
    )

    return render(request, "view_tickets_list.html", {'bugs': bugs, 'features': features})
