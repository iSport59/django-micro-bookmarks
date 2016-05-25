from django.test import TestCase
from django.test.client import Client
from bookmarks.models import *

class ViewTest(TestCase):
  fixtures = ['test_data.json']

  def setUp(self):
    self.client = Client()

  def test_register_page(self):
    data = {
      'username': 'test_user',
      'email': 'test_user@example.com',
      'password1': 'pass123',
      'password2': 'pass123'
    }
    response = self.client.post('/register/', data)
    self.assertRedirects(response, '/register/success/')

  def test_bookmark_save(self):
    response = self.client.login(
      username='ayman',
      password='1'
    )
    self.assertTrue(response)
    data = {
      'url': 'http://www.example.com/',
      'title': 'Test URL',
      'tags': 'test-tag'
    }
    response = self.client.post('/save/', data)
    self.assertRedirects(response, '/user/ayman/')

    response = self.client.get('/user/ayman/')
    self.assertContains(
      response,
      'http://www.example.com/'
    )
    self.assertContains(response, 'Test URL')
    self.assertContains(response, 'test-tag')
