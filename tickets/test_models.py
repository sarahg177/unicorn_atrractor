from django.test import TestCase
from .models import Ticket, Comments


class TestTicketModel(TestCase):
    def test_ticket_as_a_string(self):
        ticket = Ticket(title="Create a ticket")
        self.assertEqual("Create a ticket", str(ticket))

    def test_comment_as_a_string(self):
        comment = Comments(comment="This is a comment")
        self.assertEqual("This is a comment", str(comment))
