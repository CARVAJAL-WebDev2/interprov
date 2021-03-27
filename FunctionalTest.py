from selenium import webdriver
import unittest

class PageTest(unittest.TestCase):

	def setUp(self):
	   self.browser = webdriver.Firefox()
	
	def tearDown(self):
	   self.browser.quit()
	
	def test_browser_title(self):
	   self.browser.get('http://localhost:8000')
	   self.assertIn('Project List', self.browser.title)
	   self.fail('Finish the Test Now!!')
	
if __name__== '__main__':
	unittest.main(warnings='ignore')  

