from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys 
import time


class PageTest(unittest.TestCase):
	
	def setUp (self):
		self.browser = webdriver.Firefox()

	#def teardown(self):
	#	self.browser.quit()

	#def test_browser_title(self):
	#	self.browser.get('http://localhost:8000')
	#	self.assertIn('CoVid-19 Enhanced Local Travel Registration', self.browser.title)
	#	self.fail('Finish the Test!')

	def check_rows_in_listtable(self, row_text):
		table = self.browser.find_element_by_id('inList')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('CoVid-19 Enhanced Local Travel Registration', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Enhanced Local Travel Registration in compliance to CoVid-19 ', headerText)
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
		time.sleep(1)
		inName.send_keys('Edgardo Epifanio')
		time.sleep(1)
		inCode = self.browser.find_element_by_id('idUniCode')
		inCode.click()
		time.sleep(1)
		inCode.send_keys('DHG-852LKJ-CXV')
		time.sleep(1)
		inLoc = self.browser.find_element_by_id('idLocEntry')
		inLoc.click()
		time.sleep(1)
		inLoc.send_keys('Palawan')
		time.sleep(1)
		btnCon = self.browser.find_element_by_id('btnConfirm')
		time.sleep(2)
		btnCon.click()
		time.sleep(2)
		self.check_rows_in_listtable('1: Edgardo Epifanio DHG-852LKJ-CXV Palawan')
		#
		inName = self.browser.find_element_by_id('idName')
		inName.click()
		time.sleep(1)
		inName.send_keys('Filomena Sanchez')
		time.sleep(1)
		inCode = self.browser.find_element_by_id('idUniCode')
		inCode.click()
		time.sleep(1)
		inCode.send_keys('HGF-523PKL-PKN')
		time.sleep(1)
		inLoc = self.browser.find_element_by_id('idLocEntry')
		inLoc.click()
		time.sleep(1)
		inLoc.send_keys('Cebu')
		time.sleep(1)
		btnCon = self.browser.find_element_by_id('btnConfirm')
		time.sleep(2)
		btnCon.click()
		time.sleep(2)
		self.check_rows_in_listtable("2: Filomena Sanchez HGF-523PKL-PKN Cebu")
		#table = self.browser.find_element_by_id('listTable')
		#rows = table.find_elements_by_tag_name('tr')
		#self.assertIn('1: Edgardo Epifanio (DHG-852LKJ-CXV) from Palawan', [row.text for row in rows])
		#self.assertIn('2: Leona Krookroo (WRT-JHA852-KLN) from Cebu', [row.text for row in rows])
		#sefl.fail('Finish the Test!')

if __name__== '__main__':
	unittest.main(warnings='ignore')  

#def teardown(self):
	#	self.browser.quit()

	#def test_browser_title(self):
	#	self.browser.get('http://localhost:8000')
	#	self.assertIn('CoVid-19 Enhanced Local Travel Registration', self.browser.title)
	#	self.fail('Finish the Test!')
	

#browser = webdriver.Firefox()
# browser.get('http://127.0.0.8000')