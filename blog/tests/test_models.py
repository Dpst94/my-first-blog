from django.test import TestCase
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from blog.models import Post, Comment
from datetime import datetime


class PostTestCase(TestCase):
    def setUp(self):
        self.author = User(id=1)

    def test_sets_value(self):
        post = Post.objects.create(text="kort stukje.", author=self.author)
        self.assertEqual(post.text,"kort stukje.")

    def test_can_be_published(self):
        post = Post.objects.create(author=self.author)
        post.publish()
        id = post.id

        post = Post.objects.get(pk=id)
        self.assertIsInstance(post.published_date, datetime)

    def test_approved_comments(self):
        post = Post.objects.create(author=self.author)
        comment = Comment.objects.create(post=post)
        comment.approve()
        id = comment.id

        approved_comments = post.approved_comments()


class CommentTestCase(TestCase):
    def setUp(self):
        author_post = User(id=1)
        self.post = Post(author=author_post)
        self.post.save()

    def test_sets_value(self):
        comment = Comment.objects.create(text="commentaar", post=self.post)
        self.assertEqual(comment.text,"commentaar")

    def test_can_be_approved(self):
        comment = Comment.objects.create(post=self.post)
        comment.approve()
        id = comment.id

        comment = Comment.objects.get(pk=id)
        self.assertTrue(comment.approved_comment)



