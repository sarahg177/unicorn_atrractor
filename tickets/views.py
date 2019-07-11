from django.shortcuts import render
from django.utils import timezone
from tickets.models import Ticket
from .forms import CommentForm


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


def view_ticket_details(request):
    """Create a view that will return a single ticket object based on the ticket ID
    and render it to the 'view_single_ticket.html' template showing comments made."""
    ticket = Ticket.objects.get(id=request.GET.get('id'))
    form = CommentForm()

    return render(request, "view_single_ticket.html", {'ticket': ticket}, {'form': form})
