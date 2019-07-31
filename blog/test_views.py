from django.test import TestCase, Client
from users.models import User
from .models import Post


class TestBlogViews(TestCase):
    def setUp(self):
        """Set up a temporary user and blog for testing purposes"""
        self.user = User.objects.create(
            username="Joe",
            password="bloggsbloggs"
        )
        self.client = Client()

        self.blog = Post.objects.create(
            title="Create a blog",
            content='Blog contents',
            author=self.user)

    def test_get_posts(self):
        """Tests to ensure the blog posts load correctly"""
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpost.html")

    def test_create_new_post(self):
        """Tests to ensure the user can create a new post"""
        user = self.user
        page = self.client.get("/new_post/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpostform.html")
