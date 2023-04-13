from selenium.webdriver.common.by import By

# importing ConfirmationPage from pageObjects package
from pageObjects.ConfirmationPage import ConfirmationPage


class CheckoutPage:
    # tuple
    product_cards = (By.CSS_SELECTOR, ".card-title a")
    card_footers = (By.CSS_SELECTOR, ".card-footer button")
    checkout = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    confirm_checkout = (By.CSS_SELECTOR, ".btn-success")
    validate_item = (By.XPATH, "//a[text()='Blackberry']")

    # constructor
    def __init__(self, driver):
        self.driver = driver

    def get_card_titles(self):
        return self.driver.find_elements(*CheckoutPage.product_cards)   # added asterisk to deserialize the tuple

    def get_card_footers(self):
        return self.driver.find_elements(*CheckoutPage.card_footers)   # added asterisk to deserialize the tuple

    def go_to_checkout_page(self):
        return self.driver.find_element(*CheckoutPage.checkout)   # added asterisk to deserialize the tuple

    def confirm_item(self):
        return self.driver.find_element(*CheckoutPage.validate_item)   # added asterisk to deserialize the tuple

    # optimize and integrate object creation here instead of putting it in test_e2e.py
    def go_to_confirmation_page(self):
        self.driver.find_element(*CheckoutPage.confirm_checkout).click()   # added asterisk to deserialize the tuple
        confirmation_page = ConfirmationPage(self.driver)
        return confirmation_page


