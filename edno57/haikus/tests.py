from django.utils import unittest
from django.test.client import Client
from django.contrib.auth.models import User
from haikus.models import Haiku


class HaikuTest(unittest.TestCase):
    def setUp(self):
        self.user, is_new = User.objects.get_or_create(username='vanko')
        if is_new:
            self.user.set_password('parola')
            self.user.save()
        self.client = Client()
        self.client.login(username='vanko', password='parola')

    def test_login(self):
        result = self.client.get('/')
        self.assertEqual(self.user, result.context['user'])

    def test_add_haiku(self):
        haiku_text = "На клон изсъхнал настръхнали са птици след силна буря."
        result = self.client.post('', {'text': haiku_text})
        self.assertEqual(200, result.status_code)
        result = self.client.get('/')
        self.assertTrue(haiku_text.encode('UTF-8') in result.content)

    def test_loggedout_add_haiku(kiril):
        c = Client()

        count_before = Haiku.objects.all().count()
        haiku_text = "This is my non-Cyrillic haiku"
        c.post('', {'text': haiku_text})
        count_after = Haiku.objects.all().count()

        kiril.assertEqual(count_before, count_after)
