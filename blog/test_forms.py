from django.test import TestCase
from .forms import BlogPostForm

class TestBlogPostForm(TestCase):
    def test_can_create_a_blog(self):
        form = BlogPostForm({'title': 'Create a Blog', 'content': 'Blog content'})
        self.assertTrue(form.is_valid())
