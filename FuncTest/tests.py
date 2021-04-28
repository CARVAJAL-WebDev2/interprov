from selenium import webdriver
#import unittest
from selenium.webdriver.common.keys import Keys 
import time
from django.test import LiveServerTestCase
from selenium.common.exceptions import WebDriverException

cWait = 3


class PageTest(LiveServerTestCase):
	
	def setUp (self):
		self.browser = webdriver.Firefox()

	#def teardown(self):
	#	self.browser.quit()

	#def test_browser_title(self):
	#	self.browser.get('http://localhost:8000')
	#	self.assertIn('CoVid-19 Enhanced Local Travel Registration', self.browser.title)
	#	self.fail('Finish the Test!')

	def wait_rows_in_listtable(self, row_text):
		start_time = time.time()
		while time.time()-start_time<cWait:
			time.sleep(0.1)
			try:
				table = self.browser.find_element_by_id('inList')
				rows = table.find_elements_by_tag_name('tr')
				self.assertIn(row_text, [row.text for row in rows])
				return
			except (AssertionError, WebDriverException) as e:
				if time.time()-start_time>cWait:
					raise e
				time.sleep(0.5)

		#table = self.browser.find_element_by_id('inList')
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertIn(row_text, [row.text for row in rows])

	def test_start_a_list_and_retrieve_it_later(self):
		self.browser.get(self.live_server_url)
		self.assertIn('New Normal PH', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Inter-Provincial Tourist Destination Tracker', headerText)
		sectionText = self.browser.find_element_by_tag_name('label').text
		self.assertIn('Tourist Personal Information', sectionText)
		inName = self.browser.find_element_by_id('idName')
		inCode = self.browser.find_element_by_id('idUniCode')
		inLoc = self.browser.find_element_by_id('idLocEntry')
		self.assertEqual(inName.get_attribute('placeholder'),'Full Name')
		self.assertEqual(inCode.get_attribute('placeholder'),'Swab Test Result Code')
		self.assertEqual(inLoc.get_attribute('placeholder'),'Preferred Local Destination')
		inName = self.browser.find_element_by_id('idName')
		inName.click()
		inName.send_keys('Edgardo Epifanio')
		time.sleep(.1)
		inCode = self.browser.find_element_by_id('idUniCode')
		inCode.click()
		inCode.send_keys('DHG-852LKJ-CXV')
		time.sleep(.1)
		inLoc = self.browser.find_element_by_id('idLocEntry')
		inLoc.click()
		inLoc.send_keys('Palawan')
		time.sleep(.1)
		btnCon = self.browser.find_element_by_id('btnConfirm')
		btnCon.click()
		#
		time.sleep(.1)
		inName = self.browser.find_element_by_id('idName')
		inName.click()
		inName.send_keys('Filomena Sanchez')
		time.sleep(.1)
		inCode = self.browser.find_element_by_id('idUniCode')
		inCode.click()
		inCode.send_keys('HGF-523PKL-PKN')
		time.sleep(.1)
		inLoc = self.browser.find_element_by_id('idLocEntry')
		inLoc.click()
		inLoc.send_keys('Cebu')
		time.sleep(.1)
		btnCon = self.browser.find_element_by_id('btnConfirm')
		btnCon.click()
		self.wait_rows_in_listtable("2: Filomena Sanchez") # HGF-523PKL-PKN Cebu")
		self.wait_rows_in_listtable('1: Edgardo Epifanio')# DHG-852LKJ-CXV Palawan')
		#table = self.browser.find_element_by_id('listTable')
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertIn('chuchu', [row.text for row in rows])
		#self.assertIn('1: Edgardo Epifanio (DHG-852LKJ-CXV) from Palawan', [row.text for row in rows])
		#self.assertIn('2: Leona Krookroo (WRT-JHA852-KLN) from Cebu', [row.text for row in rows])
		#return
		#self.fail('Finish the Test!')
	# def test_multiple_users_can_start_lists_at_different_urls(self):
	# 	self.browser.get(self.live_server_url)
	# 	inName = self.browser.find_element_by_id('idName')
	# 	inName.click()
	# 	inName.send_keys('Maria Regalado')
	# 	time.sleep(.1)
	# 	inCode = self.browser.find_element_by_id('idUniCode')
	# 	inCode.click()
	# 	inCode.send_keys('YUP-OKJ874-LKI')
	# 	time.sleep(.1)
	# 	inLoc = self.browser.find_element_by_id('idLocEntry')
	# 	inLoc.click()
	# 	inLoc.send_keys('Masbate')
	# 	time.sleep(.1)
	# 	btnCon = self.browser.find_element_by_id('btnConfirm')
	# 	btnCon.click()
	# 	self.wait_rows_in_listtable('1: Maria Regalado')
	# 	#first unique URL
	# 	listview_url = self.browser.current_url
	# 	self.assertRegex(listview_url, '/OpenTourList/.+')
	# 	#New Browser Session
	# 	self.browser.quit()
	# 	self.browser = webdriver.Firefox()

	# 	self.browser.get(self.live_server_url)
	# 	text_page = self.browser.find_element_by_tag_name('body').text
	# 	self.assertNotIn('Maria Regalado', text_page)

	# 	time.sleep(.1)
	# 	inName = self.browser.find_element_by_id('idName')
	# 	inName.click()
	# 	inName.send_keys('George Bullock')
	# 	time.sleep(.1)
	# 	inCode = self.browser.find_element_by_id('idUniCode')
	# 	inCode.click()
	# 	inCode.send_keys('PKL-IHN874-PLK')
	# 	time.sleep(.1)
	# 	inLoc = self.browser.find_element_by_id('idLocEntry')
	# 	inLoc.click()
	# 	inLoc.send_keys('Siargao')
	# 	time.sleep(.1)
	# 	btnCon = self.browser.find_element_by_id('btnConfirm')
	# 	btnCon.click()
	# 	self.wait_rows_in_listtable('2: George Bullock')
		
	# 	#second unique URL
	# 	userview2_url = self.browser.current_url
	# 	self.assertRegex(userview2_url, '/OpenTourList/.+')
	# 	self.assertNotEqual(userview2_url, listview_url)
	# 	text_page = self.browser.find_element_by_tag_name('body').text
	# 	self.assertNotIn('Maria Regalado', text_page)
	# 	self.assertIn('George Bullock', text_page)

# if __name__== '__main__':
# 	unittest.main(warnings='ignore')  

#def teardown(self):
	#	self.browser.quit()

	#def test_browser_title(self):
	#	self.browser.get('http://localhost:8000')
	#	self.assertIn('CoVid-19 Enhanced Local Travel Registration', self.browser.title)
	#	self.fail('Finish the Test!')
	

#browser = webdriver.Firefox()
# browser.get('http://127.0.0.8000')