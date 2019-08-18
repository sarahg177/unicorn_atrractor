from django.test import TestCase, Client
from users.models import User
from .models import Post


class TestBlogViews(TestCase):
    def setUp(self):
        """Set up a temporary user and blog for testing purposes"""
        self.client = Client()

        self.user = User.objects.create(
            username="Joe",
            password="bloggsbloggs"
        )

        self.blog = Post.objects.create(
            title="Create a blog",
            content='Blog contents',
            author=User.objects.create(username="Gordon", password="bloggsbloggs"))

    def test_get_posts(self):
        """Tests to ensure the blog posts load correctly"""
        page = self.client.get("/blog/")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpost.html")

    def test_create_new_post_page_view(self):
        """Tests the view for create a new post page renders correctly"""
        User.objects.create(username="Fred", password="bloggsbloggs")
        page = self.client.get("/blog/new_post")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpostform.html")

    # def test_post_create_new_a_post_in_blog(self):
    #     User.objects.filter('Joe')
    #     request = self.client.post('/blog/new_post', {'title': 'a new blog', 'content': 'blog content'})
    #
    #     self.assertEqual(request.status_code, 302)
