#from django.urls import resolve
from django.test import TestCase
#from OpenTourList.views import Mainpage
#from django.http import HttpRequest
#from django.template.loader import render_to_string


class HomePageTest(TestCase):

	def test_root_url_resolves_to_mainpage_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', data = {'idName': 'newTouristName'})
		self.assertIn('newTouristName', response.content.decode())
		self.assertTemplateUsed(response, 'mainpage.html')

'''	
	def test_root_url_resolves_to_mainpage_view(self):
		found = resolve('/')
		self.assertEqual(found.func, Mainpage)
		self.assertTrue(html.startswith('<html>'))
		self.assertIn(html.startswith('<title> CoVid-19 Enhanced Local Travel Registration </title>'))
		self.assertTrue(html.endswith('</html>'))

	def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		request = HttpRequest()
		response = Mainpage(request)
		html = response.content.decode('utf8')
		self.assertEqual(html, string_html)
		self.assertTemplateUsed(response, 'mainpage.html') '''