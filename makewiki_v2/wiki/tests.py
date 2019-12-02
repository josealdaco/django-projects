import unittest
from django.test import TestCase, Client
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from wiki.models import Page
from wiki.views import CreatePage
# Create your tests here.


class WikiTestCase(TestCase):
    def test_true_is_true(self):
        """ Tests that True equals True"""
        self.assertEqual(True, True)

    def test_page_slugify_on_save(self):
        """ Tests the slug generated when saving a page"""
        # Create a user for this test
        user = User()
        user.save()
        #  Create and save Page to DB.
        page = Page(title="My Test Page", content="test", author=user)
        page.save()
        self.assertEqual(page.slug, 'my-test-page')


#  Intergration Tests with routes
class PageListViewTests(TestCase):
    """ Tests that the hompage Works"""
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create(username="siko408", email="nothing34@gmail.com", password="1234becoming")

    def test_multiple_pages(self):
        # Create a user for this test.
        user = User.objects.create()
        Page.objects.create(title="My Test Page", content="test", author=user)
        Page.objects.create(title="My Next Page Test", content="test", author=user)
        #  Mkae a GET request
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_single_page(self):
        """ Tests if the page created matches the page recieved, matching both context and status_code"""
        user = User.objects.create()
        Page.objects.create(title="The Void Inside", content="nothing here", author=user)
        Page.objects.create(title="The Light in me", content="nothing here", author=user)
        Page.objects.create(title="Work and create a company", content="nothing here", author=user)
        response = self.client.get('/')

        theLight = response.context['pages'].get(title="The Light in me")
        self.assertEqual(response.status_code, 200)  # Checking we successfully retrieved a page
        self.assertEqual(theLight.content, "nothing here") # Checking that the content matches above

    def test_createForm(self):
        """  Test the createPage form status_code"""
        user = User.objects.create()
        user.save()
        response = self.client.get('/pageCreate')
        self.assertEqual(response.status_code, 200)

    def test_create_new_page(self):
        """  Test if we can successfully create a Page"""
        '''A new page is created after the user submits the creation form.'''
        form = self.client.get("/pageCreate")
        form['title'] = "NOTHING HERE"
        form['author'] = "1"  # Choose user based on number line
        form['content'] = "this will fill the blanks"
        response = self.client.post("/pageCreate", form)
        self.assertEqual(response.status_code, 302)
