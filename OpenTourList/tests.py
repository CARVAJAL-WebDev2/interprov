from django.urls import resolve
from django.test import TestCase
from OpenTourList.views import MainPage
from django.http import HttpRequest


class HomePageTest(TestCase):

	def test_root_url_resolves_to_mainpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, MainPage)

	def test_mainpage_returns_correct_view(self):
		request = HttpRequest()
		response = MainPage(request)
		html = response.content.decode('utf8')
		self.assertTrue(html.strip().startswith('<html>'))
		self.assertIn('<title> CoVid-19 Enhanced Local Travel Registration </title>', html)
		self.assertTrue(html.strip().endswith('</html>'))