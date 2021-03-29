from selenium import webdriver
import unittest
#rom selenium.webdriver.common.keys import Keysimport time

class PageTest(unittest.TestCase):
	
	def setUp (self):
		self.browser = webdriver.Firefox()

	#def tearDown(self):
	#	self.browser.quit()

	def test_browser_title(self):
		self.browser.get('http://localhost:8000')
		self.assertIn('Open Tourist Spots', self.browser.title)
		#self.fail('Finish the Test')

if __name__== '__main__':
	unittest.main(warnings='ignore')  

"""def test_start_list_and_retrieve_it(self):
		self.browser.get('http://localhost.8000')
		self.assertIn('Open Tourist Spots',self.browser.title)
		headerText+self.browser.find_element_by_tag_name('h1').text
		self.assertIn('Open Tourist Spots', headerText)
		inputbox = self.browser.find_element_by_id('idLocEntry')
		self.assertEqual(inputbox.get_attribute('placeholder'),'Enter your preferred tourist spot')
		inputbox.send_keys('Palawan')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)
		table = self.browser.find_element_by_id('idListTable')
		rows = table.find_element_by_tag_name('tr')
		self.assertTrue(any(row.text == '1: Palawan'))
		self.fail('Finish the Test')



class PageTest(unittest.TestCase):

	def setUp(self):
	   self.browser = webdriver.Firefox()
	
	def tearDown(self):
	   self.browser.quit()
	
	def test_browser_title(self):
	   self.browser.get('http://localhost:8000')
	   self.assertIn('Project List', self.browser.title)
	   self.fail('Finish the Test Now!!')
	
"""