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

    def test_get_create_new_post_page_view(self):
        """Tests the view for create a new post page renders correctly"""
        User.objects.create(username="Fred", password="bloggsbloggs")
        page = self.client.get("/blog/new_post")
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpostform.html")

    def test_get_edit_post_page_view(self):
        """Tests the view for edit a post page renders correctly"""
        User.objects.create(username="Zebra", password="bloggsbloggs")
        self.client.login(username="Zebra", password="bloggsbloggs")
        post = Post.objects.create(title='Create a test', author_id='1')
        self.assertEqual(post.title, 'Create a test')
        page = self.client.get("/blog/edit_post?id={0}".format(post.id))
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, "blogpostform.html")
        post.save()

    def test_post_create_new_a_post_in_blog(self):
        User.objects.create(username="Fred", password="bloggsbloggs")
        Post.author = self.client.login(username="Fred", password="bloggsbloggs")
        response = self.client.post('/blog/new_post', {'title': 'a new blog', 'content': 'blog content'}, self.id())
        self.assertEqual(response.status_code, 200)

    def test_delete_blog(self):
        User.objects.create(username="Fred", password="bloggsbloggs")
        Post.author = self.client.login(username="Fred", password="bloggsbloggs")
        post = Post.objects.create(title='Create a test', content='Test blog content', author_id='1')
        post.save()
        self.assertEqual(Post.objects.count(), 2)
        response = self.client.get("/blog/delete_blog?id={0}".format(post.id))
        post.delete()
        self.assertEqual(Post.objects.count(), 1)
        self.assertEqual(response, '/blog/', status_code=200)
