from django.test import TestCase
from .models import Post


class TestPostModel(TestCase):
    def test_post_as_a_string(self):
        post = Post(title="Create a blog")
        self.assertEqual("Create a blog", str(post))

