# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_project(self):
        success = True
        wd = self.open_home_page()
        self.login(wd)
        self.create_new_project(wd, name="test-12", description="des-12")
        self.logout()


    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def create_new_project(self, wd, name, description):
        wd.find_element_by_css_selector("input.button").click()
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_xpath("//table[3]/tbody/tr[1]/td/form/input[2]").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(description)
        wd.find_element_by_css_selector("input.button").click()

    def login(self, wd):
        wd.find_element_by_name("username").click()
        wd.find_element_by_name("username").clear()
        wd.find_element_by_name("username").send_keys("administrator")
        wd.find_element_by_name("password").click()
        wd.find_element_by_name("password").clear()
        wd.find_element_by_name("password").send_keys("root")

    def open_home_page(self):
        wd = self.wd
        wd.get("http://localhost:8080/mantisbt-1.2.19/login_page.php")
        return wd

    def tearDown(self):
        self.wd.quit()


