from selenium import webdriver
import unittest

from selenium.webdriver.common.keys import Keys 
import time

class PageTest(unittest.TestCase):
	
	def setUp (self):
		self.browser = webdriver.Firefox()

	def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('CoVid-19 Enhanced Local Travel Registration', self.browser.title)
		headerText = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Enhanced Local Travel Registration in compliance to CoVid-19 ', headerText)
		sectionText = self.browser.find_element_by_tag_name('h2').text
		self.assertIn('Tourist Personal Information', sectionText)
		inputname = self.browser.find_element_by_id('idName')
		self.assertEqual(inputname.get_attribute('placeholder'),'Lastname, Firstname, M.I.')
		inputname.send_keys('Dela Cruz, Juana R.')
		inputname.send_keys(Keys.ENTER)
		time.sleep(1)
		inputcode = self.browser.find_element_by_id('idUniCode')
		self.assertEqual(inputcode.get_attribute('placeholder'),'Swab Test Result Code')
		inputcode.send_keys('DHG-852LKJ-CXV')
		inputcode.send_keys(Keys.ENTER)
		time.sleep(1)
		inputloc1 = self.browser.find_element_by_id('idLocEntry1')
		self.assertEqual(inputloc1.get_attribute('placeholder'),'Input your preferred local destination')
		inputloc1.send_keys('Cebu')
		inputloc1.send_keys(Keys.ENTER)
		btnConfirm = self.browser.find_element_by_id('btnConfirm')
		btnConfirm.click()

if __name__== '__main__':
	unittest.main(warnings='ignore')  
