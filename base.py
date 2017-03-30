import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

AUTOCOMPLETE_TIMEOUT = 10

class Page(object):

    def __init__(self, driver):

        self.driver = driver
        self.timeout = 30
 
    def find_element(self, locator):

        return self.driver.find_element(*locator)

    def wait_visibility_of_element(self, locator):

        return  WebDriverWait(self.driver, AUTOCOMPLETE_TIMEOUT).until(
            EC.visibility_of_element_located((locator)))

    def get_text(self, field_locator):

        get_text = self.driver.find_element(*field_locator).text
        return get_text



