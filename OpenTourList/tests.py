#from django.urls import resolve
from django.test import TestCase
#from OpenTourList.views import Mainpage
#from django.http import HttpRequest
#from django.template.loader import render_to_string
from OpenTourList.models import Item


class HomePageTest(TestCase):

	def test_root_url_resolves_to_mainpage_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

	def test_only_saves_items_if_necessary(self):
		self.client.get('/')
		self.assertEqual(Item.objects.count(), 0)

	def test_save_POST_request(self):
		response = self.client.post('/', data = {'idName': 'newTouristName'})
		#self.assertIn('newTouristName', response.content.decode())
		#self.assertTemplateUsed(response, 'mainpage.html')
		self.assertEqual(Item.objects.count(), 1)
		itemName = Item.objects.first()
		self.assertEqual(itemName.text, 'newTouristName')

	def test_redirects_after_POST(self):
		response = self.client.post('/', data = {'idName': 'newTouristName'})
		self.assertEqual(response.status_code, 302)
		self.assertEqual(response['location'], '/OpenTourList/listview_url/')

	def test_template_displays_list(self):
		Item.objects.create(text = 'Entry List 1')
		Item.objects.create(text = 'Entry List 2')
		response = self.client.get('/')
		self.assertIn('Entry List 1', response.content.decode())
		self.assertIn('Entry List 2', response.content.decode())

class ORMUnitTest(TestCase):
	def test_saving_retrieving_list(self):
		entryName = Item()
		entryName.text = 'Item one'
		entryName.save()
		#Item2 = Item()
		#Item2.text = 'Item two'
		#Item2.save()
		savedItems = Item.objects.all()
		self.assertEqual(savedItems.count(), 1)
		entryName = savedItems[0]
		#savedItem2 = savedItems[1]
		self.assertEqual(entryName.text, 'Item one')
		#self.assertEqual(savedItem2.text, 'Item two')
class ViewTest(TestCase):
	def test_displays_all(self):
		Item.objects.create(text='Kennedy Reeks')
		Item.objects.create(text='Samantha Bragais')
		response = self.client.get('/OpenTourList/listview_url/')
		self.assertContains(response, 'Kennedy Reeks')
		self.assertContains(response, 'Samantha Bragais')

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