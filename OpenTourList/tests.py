from django.urls import resolve
from django.test import TestCase
from OpenTourList.views import MainPage
from django.http import HttpRequest

# Create your tests here.
class HomePageTest(TestCase):
	def test_root_url_resolves_to_mainpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, MainPage)

	def test_mainpage_returns_correst_view(self):
		request = HttpRequest()
		response = MainPage(request)nj
		html = response.content.decode('utf8')
		self.assertTrue(html.startswith('<html>'))
		self.assertIn('<title> Open Tourist Spots List </title>', html)
		self.assertTrue(html.endswith('</html>'))