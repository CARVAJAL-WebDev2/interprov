from django.test import TestCase
from .models import Item, Tourist
from .views import MainPage, ViewersList, NewestList, AddSomeItem

class HomePageTest(TestCase):
	def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response, 'mainpage.html')

class ORMUnitTest(TestCase):
	def test_saving_retrieving_list(self):
		newTourist = Tourist()
		newTourist.save()
		exName1 = Item()
		exName1.text = 'Unang Item'
		exName1.TourId = newTourist
		exName1.save()
		exName2 = Item()
		exName2.text = 'Pangalawang Item'
		exName2.TourId = newTourist
		exName2.save()
		savedNames = Item.objects.all()
		savedTourist = Tourist.objects.first()
		self.assertEqual(savedNames.count(), 2)
		self.assertEqual(savedTourist, newTourist)
		savedName1 = savedNames[0]
		savedName2 = savedNames[1]
		self.assertEqual(savedName1.text, 'Unang Item')
		self.assertEqual(savedName2.text, 'Pangalawang Item')
		self.assertEqual(savedName1.TourId, newTourist)
		self.assertEqual(savedName2.TourId, newTourist)

class ListViewTest(TestCase):
	def test_displays_each_tourist(self):
		newTourist = Tourist.objects.create()
		Item.objects.create(TourId=newTourist, text='Ken')
		Item.objects.create(TourId=newTourist, text='Sam')
		response = self.client.get(f'/OpenTourList/{newTourist.id}/')
		self.assertContains(response, 'Ken')
		self.assertContains(response, 'Sam')

		newTourist2 = Tourist.objects.create()
		Item.objects.create(TourId=newTourist2, text='Stef')
		Item.objects.create(TourId=newTourist2, text='Harp')
		response = self.client.get(f'/OpenTourList/{newTourist2.id}/')
		self.assertContains(response, 'Stef')
		self.assertContains(response, 'Harp')

	def test_listview_uses_listpage(self):
		newTourist = Tourist.objects.create()
		response = self.client.get(f'/OpenTourList/{newTourist.id}/')
		self.assertTemplateUsed(response,'listpage.html')

	def test_pass_list_to_template(self):
		ExList1 = Tourist.objects.create()
		ExList2 = Tourist.objects.create()
		listPass = Tourist.objects.create()
		response = self.client.get(f'/OpenTourList/{listPass.id}/')
		# self.assertEqual(response.context['TourId'], listPass)

class CreateListTest(TestCase):
	def test_save_POST_request(self):
		response = self.client.post('/OpenTourList/newlist_url',data={'idName':'New Entry'})	
		newItem = Item.objects.first()
		# self.assertEqual(newItem.text, 'New Entry')
		# self.assertEqual(Item.objects.count(), 1)

	def test_redirects_POST(self):
		response = self.client.post('/OpenTourList/newlist_url',data={'idName':'New Entry'})
		newList = Tourist.objects.first()
		# self.assertRedirects(response, f'/OpenTourList/{newList.id}/')

class AddItemTest(TestCase):
	def test_add_POST_request_to_existing_list(self):
		DummyList1 = Tourist.objects.create()
		DummyList2 = Tourist.objects.create()
		existingList = Tourist.objects.create()
		self.client.post(f'/OpenTourList/{existingList.id}/addItem', data={'idName': 'New Item for Existing List'})
		newItem = Item.objects.first()
		# self.assertEqual(newItem.text, 'New Item for Existing List')
		# self.assertEqual(newItem.TourId, existingList)
		# self.assertEqual(Item.objects.count(),1)

	def test_redirects_to_list_view(self):
	 	DummyList1 = Tourist.objects.create()
	 	DummyList2 = Tourist.objects.create()
	 	DummyList3 = Tourist.objects.create()
	 	existingList = Tourist.objects.create()
	 	response = self.client.post(f'/OpenTourList/{existingList.id}/addItem', data={'idName': 'New Item for Existing List'})
	 	# self.assertRedirects(response, f'/OpenTourList/{existingList.id}/')	



#from django.urls import resolve
#from OpenTourList.views import Mainpage
#from django.http import HttpRequ
#from django.template.loader import render_to_string
	
		# self.assertEqual(response.status_code, 302)
		# self.assertEqual(response['location'], '/OpenTourList/listview_url/')

		# newTourist = Tourist.objects.create()
		# response = self.client.get(f'/OpenTourList/{newTourist.id}/')
		# self.assertTemplateUsed(response, 'listview.html')

		#self.assertIn('newTouristName', response.content.decode())
		#self.assertTemplateUsed(response, 'mainpage.html')

		# self.assertEqual(response.status_code, 302)
		# self.assertEqual(response['location'], '/OpenTourList/listview_url/'

	# def test_displays_each_tourist(self):
	# 	newTourist = Tourist.objects.create()
	# 	Item.objects.create(TourId=newTourist, text='Kennedy Reeks')
	# 	Item.objects.create(TourId=newTourist, text='Samantha Bragais')
	# 	response = self.client.get(f'/OpenTourList/{newTourist.id}/')
	# 	self.assertContains(response, 'Kennedy Reeks')
	# 	self.assertContains(response, 'Samantha Bragais')
	# 	self.assertNotContains(response, 'Stefania Reeks')
	# 	self.assertNotContains(response, 'Harper Bragais')

	# 	newTourist2 = Tourist.objects.create()
	# 	Item.objects.create(TourId=newTourist2, text='Stefania Reeks')
	# 	Item.objects.create(TourId=newTourist2, text='Harper Bragais')
	# 	response = self.client.get(f'/OpenTourList/{newTourist2.id}/')
	# 	self.assertContains(response, 'Stefania Reeks')
	# 	self.assertContains(response, 'Harper Bragais')

		#self.assertIn('newTouristName', response.content.decode())
		#self.assertTemplateUsed(response, 'mainpage.html')

	# def test_only_saves_items_if_necessary(self):
	# 	self.client.get('/')
	# 	self.assertEqual(Item.objects.count(), 0)

	# def test_template_displays_list(self):
	# 	Item.objects.create(text = 'Entry List 1')
	# 	Item.objects.create(text = 'Entry List 2')
	# 	response = self.client.get('/')
	# 	self.assertIn('Entry List 1', response.content.decode())
	# 	self.assertIn('Entry List 2', response.content.decode())
	# def test_redirects_POST(self):
	# 	response = self.client.post('/OpenTourList/listnew_url', data = {'idName': 'newTouristName'})
	# 	self.assertRedirects(response, '/OpenTourList/listview_url/')
	# 	self.assertEqual(response.status_code, 302)
		# self.assertEqual(response['location'], '/OpenTourList/listview_url/')

 # 	def test_root_url_resolves_to_mainpage_view(self):
	# 	found = resolve('/')
	# 	self.assertEqual(found.func, Mainpage)
	# 	self.assertTrue(html.startswith('<html>'))
	# 	self.assertIn(html.startswith('<title> CoVid-19 Enhanced Local Travel Registration </title>'))
	# 	self.assertTrue(html.endswith('</html>'))

	# def test_mainpage_returns_correct_view(self):
	# 	response = self.client.get('/')
	# 	request = HttpRequest()
	# 	response = Mainpage(request)
	# 	html = response.content.decode('utf8')
	# 	self.assertEqual(html, string_html)
	# 	self.assertTemplateUsed(response, 'mainpage.html')