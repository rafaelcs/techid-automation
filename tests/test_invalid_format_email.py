import pytest
import os
import time

from selenium import webdriver
from contact_page import *
from locators import *
from base import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from faker import Faker

fake = Faker("en_US")

class TestInvalidEmail:

    def setup_class(self):

        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("http://www.techaid.co/contact-us")
        self.driver.maximize_window()

    def test_01_fill_out_form_with_invalid_email(self):

        fillForm = ContactPage(self.driver)
        fillForm.fill_out_form(fake.name(), "rafael@@gmail.com", "TEST", fake.word())

    def test_02_assert_invalid_email_message(self):

        errorMessage = ContactPage(self.driver)
        errorMessage.get_status_message_and_assert_with('Error message\nYou must enter a valid e-mail address.')

    def teardown_class(self):

        self.driver.close()

