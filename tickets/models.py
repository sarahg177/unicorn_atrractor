from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Ticket(models.Model):
    """Choices"""
    ISSUE_TYPE = [
        ('Bug', 'Bug'),
        ('Feature', 'Feature'),
    ]

    TICKET_STATUS = [
        ('Todo', 'Todo'),
        ('Doing', 'Doing'),
        ('Done', 'Done'),
    ]

    title = models.CharField(max_length=100, blank=False)

    issue_type = models.CharField(
        max_length=7,
        choices=ISSUE_TYPE,
        default='Feature'
    )

    ticket_status = models.CharField(
        max_length=5,
        choices=TICKET_STATUS,
        default='Todo'
    )

    username = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    created_date = models.DateTimeField(default=timezone.now)

    completed_date = models.DateTimeField(blank=True, null=True)

    description = models.TextField(blank=False)

    upvotes = models.ManyToManyField(User, through='Vote', related_name='voter')

    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date_voted = models.DateTimeField(default=timezone.now)


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    date_commented = models.DateTimeField(default=timezone.now)
    comment = models.CharField(max_length=1000, blank=False)