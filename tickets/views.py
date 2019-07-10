from django.shortcuts import render, get_object_or_404, redirect
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


def view_ticket_details(request, pk):
    """Create a view that will return a single ticket object based on the ticket ID(pk)
    and render it to the 'view_single_ticket.html' template showing comments made. Or return a 404 error if the post is
    not found"""
    ticket = get_object_or_404(request, pk=pk)
    ticket.views += 1
    ticket.save()
    form = CommentForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        return redirect('single_view')
    else:
        form = CommentForm()
    return render(request, "view_single_ticket.html", {'bug': ticket}, {'form': form})
