from django.test import TestCase
from django.template.loader import render_to_string


class HomePageTest(TestCase):

	def test_root_url_resolves_to_mainpage_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	def test_save_POST_request(self):
		response = self.client.post('/', data = {'idName': 'newTouristName'})
		self.assertIn('newTouristName', response.content.decode())
		self.assertTemplateUsed(response, 'mainpage.html')