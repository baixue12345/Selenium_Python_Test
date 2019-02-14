# _*_ coding:utf-8 _*_

import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
	# 类级别的初始化
		cls.driver = webdriver.Chrome()
		cls.driver.implicitly_wait(15)
		cls.driver.maximize_window()

		cls.driver.get("http://www.baidu.com")

	def test_search_by_category(self):
		self.search_field = self.driver.find_element_by_id("kw")
		self.search_field.clear()
		self.search_field.send_keys("铜钱贯".decode('utf-8'))
		self.search_field.submit()

		products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")

		self.assertEqual(9, len(products))

	def test_search_by_category1(self):
		self.search_field = self.driver.find_element_by_id("kw")
		self.search_field.clear()
		self.search_field.send_keys("铜钱贯".decode('utf-8'))
		self.search_field.submit()

		products = self.driver.find_elements_by_xpath("//div[contains(@class, 'c-abstract')]")

		self.assertEqual(9, len(products))

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()

if __name__ == '__main__':
	unittest.main(verbosity=2)