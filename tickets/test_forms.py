from django.test import TestCase
from .forms import TicketForm

class TestTicketForm(TestCase):
    def test_can_create_a_ticket(self):
        form = TicketForm({'title': 'Create a Ticket', 'description': 'Tiscket description', 'issue_type': 'Bug'})
        self.assertTrue(form.is_valid())