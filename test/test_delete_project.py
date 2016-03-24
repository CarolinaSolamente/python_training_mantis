# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class test_delete_project(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_test_delete_project(self):
        wd = self.open_home_page()
        self.login(wd)
        self.delete_project(wd)
        self.logout(wd)


    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def delete_project(self, wd):
        wd.find_element_by_css_selector("input.button").click()
        wd.find_element_by_link_text("Manage").click()
        wd.find_element_by_link_text("Manage Projects").click()
        wd.find_element_by_link_text("test").click()
        wd.find_element_by_xpath("//div[4]/form/input[3]").click()
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
