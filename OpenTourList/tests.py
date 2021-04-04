from django.test import TestCase
from django.template.loader import render_to_string


class HomePageTest(TestCase):

	def test_root_url_resolves_to_mainpage_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')