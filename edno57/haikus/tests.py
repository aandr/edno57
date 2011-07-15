# coding: utf-8
from django.utils import unittest
from django.test.client import Client
from django.contrib.auth.models import User
from haikus.models import Haiku

class HaikuTest(unittest.TestCase):
    def setUp(self):
        self.user, is_new = User.objects.get_or_create(username = 'vanko')
        if is_new:
            self.user.set_password('parola')
            self.user.save()
        self.client = Client().post('/login', {'username': 'vanko', 'password': 'parola'}).client


    def test_login(self):
        res = self.client.get('/')
        self.assertEqual(self.user, res.context['user'])

    def test_add_haiku(self):
        haiku_text = u"Това е моето хайку"
        res = self.client.post('/add', {'text': haiku_text})
        self.assertEqual(302, res.status_code)

        res = self.client.get('/')
        self.assertTrue(haiku_text in res.content)

    def test_loggedout_add_haiku(sefl):
        c = Client()

        count_before = Haiku.objects.all().count()
        haiku_text = "This is my non-Cyrillic haiku"
        res = c.post('/add', {'text': haiku_text})
        count_after = Haiku.objects.all().count()

        sefl.assertEqual(count_before, count_after)
