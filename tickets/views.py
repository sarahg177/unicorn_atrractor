from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from tickets.models import Ticket, Comments, Vote
from .forms import CommentForm, TicketForm


def welcome(request):
    return render(request, 'welcome_page.html')


def get_ticket_list(request):
    """Shows list of all tickets"""
    all_bugs = Ticket.objects.filter(
        created_date__lte=timezone.now(),
        issue_type=Ticket.Bug
    )
    bugs = all_bugs.exclude(ticket_status=Ticket.Done)
    features = Ticket.objects.filter(
        created_date__lte=timezone.now(),
        issue_type=Ticket.Feature
    )
    vote_dict = {}
    if request.user:
        votes = Vote.objects.filter(user=request.user)
        for vote in votes:
            vote_dict[vote.ticket_id] = True
    bugs_ = [(b, b.id in vote_dict) for b in bugs]
    return render(request, "view_tickets_list.html", {'bugs': bugs, 'features': features, 'votes': vote_dict})


def view_ticket_details(request):
    """Create a view that will return a single ticket object based on the ticket ID, view comments made and user can
    make comments and render it to the 'view_single_ticket.html' template showing comments made."""
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


def vote_for_ticket(request):
    """Increment vote count for bug and redirects to """
    bug_ticket = request.GET.get('id')
    bug = Ticket.objects.get(id=bug_ticket)
    user = request.user
    vote = Vote(user=user, ticket=bug)
    vote.save()
    return redirect('ticket_list')


def edit_a_bug(request):
    """Edit a ticket"""
    ticket = Ticket.objects.get(id=request.GET.get('id'))
    if request.method == "POST":
        form = TicketForm(request.POST, request.FILES, instance=ticket)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.author = request.user
            form.save()
            return redirect('ticket_list')
    else:
        form = TicketForm(instance=ticket)
    return render(request, "create_ticket.html", {'form': form})
