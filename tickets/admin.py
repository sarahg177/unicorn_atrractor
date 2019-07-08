from django.contrib import admin
from tickets.models import Ticket, Vote, Comments

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Vote)
admin.site.register(Comments)
