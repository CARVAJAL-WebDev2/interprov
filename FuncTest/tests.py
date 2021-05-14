from selenium import webdriver 
#import unittest
from selenium.webdriver.common.keys import Keys
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

cWait = 3
class PageTesting(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()
	
	def wait_rows_in_listtable(self, row_text):                                   
		start_time = time.time()
		while time.time()-start_time<cWait:
			time.sleep(0.1)
		try:
			table = self.browser.find_element_by_id('inList')
			rows = table.find_elements_by_tag_name('tr')
			self.assertIn(row_text, [row.text for row in rows])
			return
		except(AssertionError, WebDriverException) as e:
			if time.time()-start_time>cWait:
				raise e

	def test_start_list_one_user(self):
		self.browser.get(self.live_server_url)
		self.assertIn('New Normal PH', self.browser.title)
		headText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Inter-Provincial Tourist Destination Tracker', headText)
	
		inName = self.browser.find_element_by_id('idName')
		inName.click()
		inName.send_keys('Edgardo Epifanio')
		time.sleep(.1)
		inEmail = self.browser.find_element_by_id('idEmail')
		inEmail.click()
		inEmail.send_keys('epifanio.edgardo99@gmail.com')
		time.sleep(.1)
		inCode = self.browser.find_element_by_id('idUniCode')
		inCode.click()
		inCode.send_keys('DHG-852LKJ-CXV')
		time.sleep(.1)
		inOrigin = self.browser.find_element_by_id('idOrigin')
		inOrigin.click()
		inOrigin.send_keys('Imus, Cavite')
		time.sleep(.1)
		inDes = self.browser.find_element_by_id('idDestination')
		inDes.click()
		inDes.send_keys('Palawan')
		time.sleep(.1)
		inPurpose = self.browser.find_element_by_id('idPurpose')
		inPurpose.click()
		inPurpose.send_keys('Business Meeting')
		inComp = self.browser.find_element_by_id('idComp')
		inComp.click()
		inComp.send_keys('No')
		time.sleep(.1)
		inEmail = self.browser.find_element_by_id('idPets')
		inEmail.click()
		inEmail.send_keys('No')
		time.sleep(.1)
		inDes = self.browser.find_element_by_id('idHistory')
		inDes.click()
		inDes.send_keys('Imus Lumina')
		time.sleep(.1)
		btnCon = self.browser.find_element_by_id('idConfirm')
		btnCon.click()
		self.wait_rows_in_listtable('1: Edgardo Epifanio')

		time.sleep(.1)
		inName = self.browser.find_element_by_id('idName')
		inName.click()
		inName.send_keys('Mariella Arida')
		time.sleep(.1)
		inEmail = self.browser.find_element_by_id('idEmail')
		inEmail.click()
		inEmail.send_keys('maye99@gmail.com')
		time.sleep(.1)
		inCode = self.browser.find_element_by_id('idUniCode')
		inCode.click()
		inCode.send_keys('HJG-7854P-741')
		time.sleep(.1)
		inOrigin = self.browser.find_element_by_id('idOrigin')
		inOrigin.click()
		inOrigin.send_keys('Dasmarinas City, Cavite')
		time.sleep(.1)
		inDes = self.browser.find_element_by_id('idDestination')
		inDes.click()
		inDes.send_keys('Boracay')
		time.sleep(.1)
		inPurpose = self.browser.find_element_by_id('idPurpose')
		inPurpose.click()
		inPurpose.send_keys('Emergency Purpose')
		inComp = self.browser.find_element_by_id('idComp')
		inComp.click()
		inComp.send_keys('Yes, Mother')
		time.sleep(.1)
		inEmail = self.browser.find_element_by_id('idPets')
		inEmail.click()
		inEmail.send_keys('No')
		time.sleep(.1)
		inDes = self.browser.find_element_by_id('idHistory')
		inDes.click()
		inDes.send_keys('Barangay Salitran Health Center')
		time.sleep(.1)
		btnCon = self.browser.find_element_by_id('idConfirm')
		btnCon.click()
		self.wait_rows_in_listtable('2: Mariella Arida')

	def test_other_users_different_urls(self):
		self.browser.get(self.live_server_url)
		time.sleep(.1)
		inName = self.browser.find_element_by_id('idName')
		inName.click()
		inName.send_keys('Christian Dior')
		time.sleep(.1)
		inEmail = self.browser.find_element_by_id('idEmail')
		inEmail.click()
		inEmail.send_keys('chrisdior@gmail.com')
		time.sleep(.1)
		inCode = self.browser.find_element_by_id('idUniCode')
		inCode.click()
		inCode.send_keys('SDG-796PL-O54')
		time.sleep(.1)
		inOrigin = self.browser.find_element_by_id('idOrigin')
		inOrigin.click()
		inOrigin.send_keys('Makati City')
		time.sleep(.1)
		inDes = self.browser.find_element_by_id('idDestination')
		inDes.click()
		inDes.send_keys('El Nido')
		time.sleep(.1)
		inPurpose = self.browser.find_element_by_id('idPurpose')
		inPurpose.click()
		inPurpose.send_keys('Photoshoot')
		inComp = self.browser.find_element_by_id('idComp')
		inComp.click()
		inComp.send_keys('Yes, Handler and Makeup Artist')
		time.sleep(.1)
		inEmail = self.browser.find_element_by_id('idPets')
		inEmail.click()
		inEmail.send_keys('Yes')
		time.sleep(.1)
		inDes = self.browser.find_element_by_id('idHistory')
		inDes.click()
		inDes.send_keys('Makati Business District')
		time.sleep(.1)
		btnCon = self.browser.find_element_by_id('idConfirm')
		btnCon.click()
		self.wait_rows_in_listtable('1: Christian Dior')
		#first unique URL
		linkViewLink = self.browser.current_url
		self.assertRegex(linkViewLink, '/OpenTourList/.+')
		#New Browser Session
		self.browser.quit()
		self.browser = webdriver.Firefox()

		self.browser.get(self.live_server_url)
		contentPage = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Christian Dior', contentPage)

		time.sleep(.1)
		inName = self.browser.find_element_by_id('idName')
		inName.click()
		inName.send_keys('Wanda Maximoff')
		time.sleep(.1)
		inEmail = self.browser.find_element_by_id('idEmail')
		inEmail.click()
		inEmail.send_keys('scarlettwitch@gmail.com')
		time.sleep(.1)
		inCode = self.browser.find_element_by_id('idUniCode')
		inCode.click()
		inCode.send_keys('785-OPKHG-741')
		time.sleep(.1)
		inOrigin = self.browser.find_element_by_id('idOrigin')
		inOrigin.click()
		inOrigin.send_keys('WestVille')
		time.sleep(.1)
		inDes = self.browser.find_element_by_id('idDestination')
		inDes.click()
		inDes.send_keys('New Avengers HQ')
		time.sleep(.1)
		inPurpose = self.browser.find_element_by_id('idPurpose')
		inPurpose.click()
		inPurpose.send_keys('Training')
		inComp = self.browser.find_element_by_id('idComp')
		inComp.click()
		inComp.send_keys('Yes, Vision')
		time.sleep(.1)
		inEmail = self.browser.find_element_by_id('idPets')
		inEmail.click()
		inEmail.send_keys('No')
		time.sleep(.1)
		inDes = self.browser.find_element_by_id('idHistory')
		inDes.click()
		inDes.send_keys('WestVille Market')
		time.sleep(.1)
		btnCon = self.browser.find_element_by_id('idConfirm')
		btnCon.click()
		self.wait_rows_in_listtable('1: Wanda Maximoff')
		
		#second unique URL
		linkUserView2 = self.browser.current_url
		self.assertRegex(linkUserView2, '/OpenTourList/.+')
		self.assertNotEqual(linkUserView2, linkViewLink)
		contentPage = self.browser.find_element_by_tag_name('body').text
		self.assertNotIn('Christian Dior', contentPage)
		self.assertIn('Wanda Maximoff', contentPage)




