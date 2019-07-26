import json
from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Count
from datetime import timedelta
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

    return render(request, "view_tickets_list.html", {
        'bugs': bugs, 'features': features, 'votes': vote_dict})


def view_ticket_details(request):
    """Create a view that will return a single ticket object based on the ticket ID, view comments made and user can
    make comments and render it to the 'view_single_ticket.html' template showing comments made."""
    ticket = Ticket.objects.get(id=request.GET.get('id'))
    ticket.views += 1
    ticket.save()
    form = CommentForm()
    try:
        vote = Vote.objects.get(ticket=ticket, user=request.user)
    except Vote.DoesNotExist:
        vote = None

    voted_by_user = False
    if vote:
        voted_by_user = True
    if 'comment' in request.POST:
        comment = request.POST.get('comment')
        comment = Comments(user=request.user, ticket=ticket, comment=comment)
        comment.save()
    posted_comments = Comments.objects.filter(ticket=ticket)

    return render(request, "view_single_ticket.html", {
        'form': form, 'ticket': ticket, 'comments': posted_comments, 'voted': voted_by_user})


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


def vote_for_ticket(request):
    """Increment vote count for bug and redirects to """
    bug_ticket = request.GET.get('id')
    next_page = "single_view?id=" + str(bug_ticket)
    if "next" in request.GET:
        next_page = request.GET.get('next')
    bug = Ticket.objects.get(id=bug_ticket)
    bug.votes_total += 1
    bug.save()
    user = request.user
    vote = Vote(user=user, ticket=bug)
    vote.save()
    return redirect(next_page)


def feature_payment(request):
    """Increases money raised by # and redirects # to """
    feature_ticket = request.GET.get('id')
    next_page = "single_view?id=" + str(feature_ticket)
    if "next" in request.GET:
        next_page = request.GET.get('next')
    feature = Ticket.objects.get(id=request.GET.get('id'))
    feature.money_raised += 20
    feature.save()
    return redirect(next_page)


def graphs(request):
    """Renders a view for graphs"""
    """Bar chart"""
    day = timezone.now() - timedelta(days=1)
    week = timezone.now() - timedelta(days=7)
    month = timezone.now() - timedelta(days=28)

    bug_count_day = Ticket.objects.filter(
        issue_type=Ticket.Bug,
        created_date__gte=day
    ).count()

    feature_count_day = Ticket.objects.filter(
        issue_type=Ticket.Feature,
        created_date__gte=day
    ).count()

    bug_count_week = Ticket.objects.filter(
        issue_type=Ticket.Bug,
        created_date__gte=week
    ).count()

    feature_count_week = Ticket.objects.filter(
        issue_type=Ticket.Feature,
        created_date__gte=week
    ).count()

    bug_count_month = Ticket.objects.filter(
        issue_type=Ticket.Bug,
        created_date__gte=month
    ).count()

    feature_count_month = Ticket.objects.filter(
        issue_type=Ticket.Feature,
        created_date__gte=month
    ).count()

    bugs = Ticket.objects.filter(issue_type=Ticket.Bug)
    bug_title = Ticket.title

    bug_votes_count = Ticket.objects.filter(
        issue_type=Ticket.Bug,
        votes_total__gte=0
    ).count()

    highest_voted_bug_name = ""
    highest_voted_bug_count = 0
    for bug in Ticket.objects.filter(issue_type=Ticket.Bug).annotate(total_votes=Count('votes')):
        if bug.total_votes > highest_voted_bug_count:
            highest_voted_bug_count = bug.total_votes
            highest_voted_bug_name = bug.title

    highest_paid_feature_ticket = Ticket.objects.filter(issue_type=Ticket.Feature, created_date__lte=timezone.now())
    highest_paid_feature_name = ""
    highest_paid_feature_amount = 0
    for feature in highest_paid_feature_ticket:
        if feature.money_raised > highest_paid_feature_amount:
            highest_paid_feature_amount = feature.money_raised
            highest_paid_feature_name = feature

    return render(request, "graphs.html", {
        'bug_count_day': bug_count_day,
        'feature_count_day': feature_count_day,
        'bug_count_week': bug_count_week,
        'feature_count_week': feature_count_week,
        'bug_count_month': bug_count_month,
        'feature_count_month': feature_count_month,
        'bugs': bugs,
        'bug_title': bug_title,
        'bug_votes_count': bug_votes_count,
        'highest_voted_bug_count': highest_voted_bug_count,
        'highest_voted_bug_name': highest_voted_bug_name,
        'highest_paid_feature_amount': highest_paid_feature_amount,
        'highest_paid_feature_name': highest_paid_feature_name,
    })
