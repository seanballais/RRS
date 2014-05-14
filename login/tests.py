from django.test import TestCase
from login.models import CustomUser
from django.utils import timezone
from django.core.urlresolvers import reverse


class LoginTest(TestCase):
	""" Test that will create a test user and display the username """
    def create_user(self, username = "test", password = "12345", emailadd = "testing101@testing101.com", user_privileges = 1, firstname = "Test", lastname = "Culinary"):
        return CustomUser.objects.create(username=username,password=password,emailadd=emailadd, user_privileges=user_privileges, firstname=firstname, lastname=lastname)

    def test(self):
        w = self.create_user()
        self.assertTrue(isinstance(w, Whatever))
        self.assertEqual(w.__unicode__(), w.username)