import pytest

from testData.ConfirmationPageData import ConfirmationPageData
#importing BaseClass from utilities package
from utilities.BaseClass import BaseClass
# importing HomePage from pageObjects package
from pageObjects.HomePage import HomePage


class TestOne(BaseClass):   # inherit BaseClass

    def test_e2e(self, get_data):
        # adding logging functionality by calling getLogger function from BaseClass
        log = self.getLogger()

        # click shop
        home_page = HomePage(self.driver)
        checkout_page = home_page.shop_items()

        log.info("Getting all the card titles")
        # go into the product cards xpath
        cards = checkout_page.get_card_titles()

        # iterate to all products and find Blackberry
        i = 0
        for card in cards:
            product_name = card.text
            log.info(product_name)

            # click add button if Blackberry is the product
            if product_name == "Blackberry":
                checkout_page.get_card_footers()[i].click()  # did not use div[2]/button as xpath since only 1 div has a button as a child element
                log.info("You have added " + product_name + " to the cart")
            i = i + 1


        # click checkout button
        checkout_page.go_to_checkout_page().click()
        log.info("Proceeding to Checkout page")

        # checkout page and getting the text of the added item to cart
        chosen_item = checkout_page.confirm_item().text

        # validating if the correct item is added
        assert chosen_item == "Blackberry"

        # click checkout button of checkout page to proceed to the confirmation page
        confirmation_page = checkout_page.go_to_confirmation_page()
        log.info("Entering country name as 'lan'")

        #send keys "lan"
        confirmation_page.get_country_initial().send_keys(get_data["country initial"])

        # explicit wait for 10 seconds
        self.verify_element_located(get_data["country"])   # called function in BaseClass to make the code cleaner

        # click country at auto-suggestive dropdown list
        confirmation_page.get_selected_country().click()

        # check the checkbox
        confirmation_page.mark_check_box().click()

        # click purchase button
        confirmation_page.purchase_button().click()

        # validating if success message is displayed
        success_txt = confirmation_page.validate_success().text
        log.info("Text received from application is: '" + success_txt + "'")

        assert 'Success!' in success_txt  # used keyword in to just validate a text or phrase inside a sentence.

    # used fixture here instead of putting it in conftest since this can't be used across multiple testcase
    @pytest.fixture(params=ConfirmationPageData.test_confirmation_page_data)
    def get_data(self, request):
        return request.param