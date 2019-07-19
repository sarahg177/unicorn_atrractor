from django.db import models
from django.utils import timezone
from tickets.models import Ticket
from users.models import User


class Product(models.Model):
    name = models.CharField(max_length=250, default='')
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ticket = models.ForeignKey(Ticket, on_delete=models.DO_NOTHING)
    date = models.DateField(default=timezone.now)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
