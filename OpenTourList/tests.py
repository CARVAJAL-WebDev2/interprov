from django.test import TestCase
from OpenTourList.models import Item, Tourist
	
class HomePageTest(TestCase):
	def test_mainpage_returns_correct_view(self):
		response = self.client.get('/')
		self.assertTemplateUsed(response,'mainpage.html')
		
class ORMTest(TestCase):
	def test_saving_retrieving_list(self):
		newTourist = Tourist()
		newTourist.save()
		txtItem1 = Item()
		txtItem1.text = 'Item one'
		txtItem1.TourId = newTourist
		txtItem1.save()
		txtItem2 = Item()
		txtItem2.TourId = newTourist
		txtItem2.text = 'Item two'
		txtItem2.save()
		savedItems = Item.objects.all()
		savedTourist = Tourist.objects.first()
		self.assertEqual(savedItems.count(), 2)
		self.assertEqual(savedTourist,newTourist)
		savedItem1 = savedItems[0]
		savedItem2 = savedItems[1]
		self.assertEqual(savedItem1.text, 'Item one')
		self.assertEqual(savedItem2.text, 'Item two')
		self.assertEqual(savedItem1.TourId, newTourist)
		self.assertEqual(savedItem2.TourId, newTourist)			

class ViewTest(TestCase):
	def test_displays_each_recruit(self):
		newTourist = Tourist.objects.create()
		Item.objects.create(TourId=newTourist, text='Sam')
		Item.objects.create(TourId=newTourist, text='Ken')
		response = self.client.get(f'/OpenTourList/{newTourist.id}/')
		self.assertNotContains(response, 'Lav')
		self.assertNotContains(response, 'Ion')
		
		newTourist_2 = Tourist.objects.create()
		Item.objects.create(TourId=newTourist_2, text='Lav')
		Item.objects.create(TourId=newTourist_2, text='Ion')
		response = self.client.get(f'/OpenTourList/{newTourist_2.id}/')
		self.assertNotContains(response, 'Sam')
		self.assertNotContains(response, 'Ken')

		
	def test_listview_uses_listpage(self):
		newTourist = Tourist.objects.create()
		response = self.client.get(f'/OpenTourList/{newTourist.id}/')
		self.assertTemplateUsed(response, 'listpage.html')

	def test_pass_list_to_template(self):
		dummyList1 = Tourist.objects.create()
		dummyList2 = Tourist.objects.create()
		passList = Tourist.objects.create()
		response = self.client.get(f'/OpenTourList/{passList.id}/')
		self.assertEqual(response.context['TourId'], passList)

class CreateListTest(TestCase):
	def test_save_POST_request(self):
		response = self.client.post('/OpenTourList/newlist_url',data={'idName':'New Entry'})	
		self.assertEqual(Item.objects.count(),1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'New Entry')

	def test_redirects_POST(self):
		response = self.client.post('/OpenTourList/newlist_url',data={'idName':'New Entry'})
		newList = Tourist.objects.first()
		self.assertRedirects(response, f'/OpenTourList/{newList.id}/')

class AddItemTest(TestCase):
	def test_add_POST_request_to_existing_list(self):
		DummyList1 = Tourist.objects.create()
		DummyList2 = Tourist.objects.create()
		existingList = Tourist.objects.create()
		self.client.post(f'/OpenTourList/{existingList.id}/addItem',data={'idName': 'New Item for Existing List'})
		self.assertEqual(Item.objects.count(),1)
		newItem = Item.objects.first()
		self.assertEqual(newItem.text, 'New Item for Existing List')
		self.assertEqual(newItem.TourId, existingList)

	def test_redirects_to_list_view(self):
	 	DummyList1 = Tourist.objects.create()
	 	DummyList2 = Tourist.objects.create()
	 	DummyList3 = Tourist.objects.create()
	 	existingList = Tourist.objects.create()
	 	response = self.client.post(f'/OpenTourList/{existingList.id}/addItem',data={'idName': 'New Item for Existing List'})
	 	self.assertRedirects(response, f'/OpenTourList/{existingList.id}/')		