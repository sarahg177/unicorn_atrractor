from django.test import TestCase, Client
from django.utils import timezone

from users.models import User
from .models import Post


class TestBlogViews(TestCase):
    def SetUp(self):
        """Set up a temporary user and blog for testing purposes"""
        self.user = User.objects.create(
            username="Joe",
            password="bloggsbloggs"
        )
        self.client = Client()

        self.blog = Post.objects.create(
            title="Create a blog",
            content='Blog contents',
            author=self.user,
            published_date=timezone.now())

    def test_get_posts(self):
        """Tests to ensure the blog posts load correctly"""
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpost.html")

    def test_create_a_blog(self):
        """Tests that user can create a blog and redirected to blogs list page"""
        response = self.client.post("/new_post", {
            "title": "Create a new blog",
            "content": "More blog contents",
            "author": 'Joe',
            "published_date": timezone.now()
        })

        self.assertEqual(response.status_code, 302)
        self.assertEqual()
