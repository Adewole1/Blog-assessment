from django.test import TestCase
from django.contrib.auth.models import User

from .models import BlogPost


class BlogTests(TestCase):
    
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123'
        )
        testuser1.save()

        test_post = BlogPost.objects.create(
            author=testuser1, title='Test title', body='Test body content....'
        )
        test_post.save()

    def test_blog_content(self):
        post = BlogPost.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Test title')
        self.assertEqual(body, 'Test body content....')