from django.test import TestCase, Client
from users.models import User
from .models import Ticket


class TestTicketViews(TestCase):
    def setUp(self):
        """Set up a temporary user and ticket for testing purposes"""
        self.client = Client()

        self.user = User.objects.create(
            username="Joe",
            password="bloggsbloggs"
        )

        self.ticket = Ticket.objects.create(
            title="Create a ticket",
            username=User.objects.create(username="Gordon", password="bloggsbloggs"),
            description="Ticket description"
        )

    def test_welcome_page(self):
        """Test to ensure the welcome page loads correctly"""
        page = self.client.get("/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "welcome_page.html")
