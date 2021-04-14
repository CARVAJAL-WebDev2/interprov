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

	#def check_rows_in_listtable(self, row_text):
	#	table = self.browser.find_elements_by_id('listTable')
	#	rows = table.find_element_by_tag_name('tr')
	#	self.assertIn(row_text, [row.text for row in rows])

	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('CoVid-19 Enhanced Local Travel Registration', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Enhanced Local Travel Registration in compliance to CoVid-19 ', headerText)
		sectionText = self.browser.find_element_by_tag_name('label').text
		self.assertIn('Tourist Personal Information', sectionText)
		inputname = self.browser.find_element_by_id('idName')
		inputcode = self.browser.find_element_by_id('idUniCode')
		inputloc1 = self.browser.find_element_by_id('idLocEntry1')
		btnCon = self.browser.find_element_by_id('btnConfirm')
		self.assertEqual(inputname.get_attribute('placeholder'),'Lastname, Firstname, M.I.')
		self.assertEqual(inputcode.get_attribute('placeholder'),'Swab Test Result Code')
		self.assertEqual(inputloc1.get_attribute('placeholder'),'Input your preferred local destination')
		time.sleep(2)
		inputname.send_keys('Dela Cruz, Juana R.')
		#time.sleep(1)
		#inputname.click()
		time.sleep(2)
		inputcode.send_keys('DHG-852LKJ-CXV')
		#time.sleep(1)
		#inputcode.click()
		time.sleep(2)
		inputloc1.send_keys('Cebu')
		btnCon.click()
		time.sleep(3)
		table = self.browser.find_element_by_id('listTable')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn('1: Dela Cruz, Juana R. with Swab Test Result Code DHG-852LKJ-CXV from Cebu', [row.text for row in rows])
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