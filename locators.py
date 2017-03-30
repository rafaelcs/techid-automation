from selenium.webdriver.common.by import By

class ContactPageLocators(object):

  NAME_FIELD            = (By.ID, "edit-name")
  EMAIL_FIELD           = (By.ID, "edit-mail")
  SUBJECT_FIELD         = (By.ID, "edit-subject")
  MESSAGE_FIELD         = (By.ID, "edit-message")
  SEND_MESSAGE_BUTTON   = (By.ID, "edit-submit")
  STATUS_MESSAGE         = (By.CSS_SELECTOR, "div.messages")
  FORM_FIELDS           = (By.CSS_SELECTOR, ".form-item")