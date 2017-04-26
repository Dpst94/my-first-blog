import unittest
from django.test import Client
from django.contrib.auth.models import User
from blog.models import Post, Comment

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()
        author_post = User(id=1)
        self.post = Post(author=author_post)
        self.post.publish()
        self.post2 = Post(author=author_post)
        self.post2.publish()

    def test_details(self):
        response = self.client.get('/')

        self.assertEqual(response.status_code,200)

        self.assertEqual(len(response.context['posts']),2)

    def test_more(self):
        response =self.client.get('/post/1/')
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(response.context['post'])

