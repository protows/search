# -*- coding: utf-8 -*-
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://edition.cnn.com/")
        elem_travel = driver.find_element_by_css_selector("a.nav-menu-links__link:nth-child(7)")
        elem_travel.click()
        elem_food = driver.find_element_by_css_selector("a.Header__section:nth-child(2)")
        elem_food.click()
        time.sleep(5)       
        assert "Food & Drink | CNN Travel" in driver.title

    def tearDown(self):
    	self.driver.close()

if __name__ == "__main__":
	unittest.main()











