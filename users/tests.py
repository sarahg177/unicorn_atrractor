from django.test import TestCase, Client
from .models import User


class TestUser(TestCase):
    def setUp(self):
        """Runs at the start of the test"""
        self.client = Client()

    def test_create_user(self):
        """Tests the user model"""
        User.objects.create(username='Joe', password='bloggs')
        assert len(User.objects.all()) == 1

    def test_register_view(self):
        """Test the register page renders correctly"""
        reg = self.client.get('/users/register/')
        assert b"<input" in reg.content
        assert b"username" in reg.content
        assert b"password1" in reg.content
        assert b"password2" in reg.content

    def test_registration_was_succesful(self):
        """Test that the user has registered successfully and then redirected"""
        reg = self.client.post('/users/register/', {'username': 'joe',
                                                    'password1': 'bloggsbloggs',
                                                    'password2': 'bloggsbloggs'})
        assert reg.status_code == 302
