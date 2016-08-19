from django.test import TestCase
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.


class PostTest(TestCase):

    def setUp(self):
        self.test_date = timezone.now()
        self.me = User.objects.create(username='dojo', email='', password='top_secret')
        self.post = Post.objects.create(author=self.me,
                                        title='testing',
                                        text='hello world!',
                                        creation_date=self.test_date)

    def test_author(self):
        post = Post.objects.get(author=self.me)
        self.assertEqual(post.author, self.me)

    def test_title(self):
        post = Post.objects.get(title='testing')
        self.assertEqual(post.title, 'testing')

    def test_text(self):
        post = Post.objects.get(text='hello world!')
        self.assertEqual(post.text, 'hello world!')

    def test_creation_date(self):
        post = Post.objects.get(creation_date=self.test_date)
        self.assertEqual(post.creation_date, self.test_date)


