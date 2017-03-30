import os
import time

from selenium import webdriver
from base import Page
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ContactPage(Page):

	def fill_out_form(self, enter_name, enter_email, enter_subject, enter_message):

		self.find_element(ContactPageLocators.NAME_FIELD).send_keys(enter_name)
		self.find_element(ContactPageLocators.EMAIL_FIELD).send_keys(enter_email)
		self.find_element(ContactPageLocators.SUBJECT_FIELD).send_keys(enter_name)
		self.find_element(ContactPageLocators.MESSAGE_FIELD).send_keys(enter_message)
		self.find_element(ContactPageLocators.SEND_MESSAGE_BUTTON).click()
		self.wait_visibility_of_element(ContactPageLocators.STATUS_MESSAGE)

	def get_status_message_and_assert_with(self, message):

		assert self.get_text(ContactPageLocators.STATUS_MESSAGE) == message
