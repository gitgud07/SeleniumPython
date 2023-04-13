from selenium.webdriver.common.by import By


class ConfirmationPage:
    # tuple
    country_initial = (By.CSS_SELECTOR, "#country")
    selected_country = (By.LINK_TEXT, "Poland")
    check_box = (By.CSS_SELECTOR, ".checkbox-primary")
    purchase = (By.CSS_SELECTOR, ".btn-success")
    success_message = (By.CSS_SELECTOR, ".alert-success")

    # constructor
    def __init__(self, driver):
        self.driver = driver


    def get_country_initial(self):
        return self.driver.find_element(*ConfirmationPage.country_initial)   # added asterisk to deserialize the tuple

    def get_selected_country(self):
        return self.driver.find_element(*ConfirmationPage.selected_country)   # added asterisk to deserialize the tuple

    def mark_check_box(self):
        return self.driver.find_element(*ConfirmationPage.check_box)   # added asterisk to deserialize the tuple

    def purchase_button(self):
        return self.driver.find_element(*ConfirmationPage.purchase)   # added asterisk to deserialize the tuple

    def validate_success(self):
        return self.driver.find_element(*ConfirmationPage.success_message)   # added asterisk to deserialize the tuple
