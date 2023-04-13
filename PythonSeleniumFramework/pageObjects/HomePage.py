from selenium.webdriver.common.by import By

# importing CheckoutPage from pageObjects package
from pageObjects.CheckoutPage import CheckoutPage


class HomePage:
    # tuple
    # for testcase 1
    shop = (By.CSS_SELECTOR, "a[href*='shop")
    # testcase 2
    name = (By.CSS_SELECTOR, "[name='name']")
    email = (By.CSS_SELECTOR, "[name='email']")
    password = (By.CSS_SELECTOR, "#exampleInputPassword1")
    checkbox = (By.CSS_SELECTOR, "#exampleCheck1")
    radio_button = (By.CSS_SELECTOR, "#inlineRadio1")
    gender_dropdown = (By.CSS_SELECTOR, "#exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    msg = (By.CSS_SELECTOR, ".alert-success")

    # constructor
    def __init__(self, driver):
        self.driver = driver

    # testcase 1
    # optimize and integrate object creation here instead of putting it in test_e2e.py
    def shop_items(self):
        self.driver.find_element(*HomePage.shop).click()    # added asterisk to deserialize the tuple
        checkout_page = CheckoutPage(self.driver)
        return checkout_page

    # testcase 2
    def get_name(self):
        return self.driver.find_element(*HomePage.name)   # added asterisk to deserialize the tuple

    def get_email(self):
        return self.driver.find_element(*HomePage.email)   # added asterisk to deserialize the tuple

    def get_password(self):
        return self.driver.find_element(*HomePage.password)   # added asterisk to deserialize the tuple

    def mark_checkbox(self):
        return self.driver.find_element(*HomePage.checkbox)   # added asterisk to deserialize the tuple

    def mark_radio_button(self):
        return self.driver.find_element(*HomePage.radio_button)   # added asterisk to deserialize the tuple

    def select_gender_dropdown(self):
        return self.driver.find_element(*HomePage.gender_dropdown)   # added asterisk to deserialize the tuple

    def submit_form(self):
        return self.driver.find_element(*HomePage.submit)   # added asterisk to deserialize the tuple

    def validate_message(self):
        return self.driver.find_element(*HomePage.msg)   # added asterisk to deserialize the tuple