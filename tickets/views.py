from django.shortcuts import render, redirect
from django.utils import timezone
from tickets.models import Ticket, Comments
from .forms import CommentForm, TicketForm


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
    ticket.views += 1
    ticket.save()
    form = CommentForm()
    if 'comment' in request.POST:
        comment = request.POST.get('comment')
        comment = Comments(user=request.user, ticket=ticket, comment=comment)
        comment.save()
    posted_comments = Comments.objects.filter(ticket=ticket)

    return render(request, "view_single_ticket.html", {'form': form, 'ticket': ticket, 'comments': posted_comments})


def create_a_new_ticket(request):
    """View to allow new ticket to be added"""
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.username = request.user
            ticket.save()
            return redirect('ticket_list')
    else:
        form = TicketForm()
    return render(request, "create_ticket.html", {'form': form})
