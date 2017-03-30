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

class TestEmailSent:

    def setup_class(self):

        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get("http://www.techaid.co/contact-us")
        self.driver.maximize_window()

    def test_01_fill_out_form_with_valid_data(self):

        fillForm = ContactPage(self.driver)
        fillForm.fill_out_form(fake.name(), fake.email(), "TEST", fake.word())

    def test_02_assert_email_is_sent(self):

        successMessage = ContactPage(self.driver)
        successMessage.get_status_message_and_assert_with('Status message\nYour message has been sent.')

    def teardown_class(self):

        self.driver.close()
