import pytest

# importing HomePage class from pageObjects package
from pageObjects.HomePage import HomePage

# importing HomePageData class from testData package
from testData.HomePageData import HomePageData

# importing BaseClass class from utilities package
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_form_submission(self, get_data):
        # adding logging functionality by calling getLogger function from BaseClass
        log = self.getLogger()

        # log the displayed name
        log.info("Name is " + get_data["name"])

        # sending keys to name text field
        home_page = HomePage(self.driver)
        home_page.get_name().send_keys(get_data["name"])

        # sending keys to email text field
        home_page.get_email().send_keys(get_data["email"])

        # sending keys to password text field
        home_page.get_password().send_keys(get_data["password"])

        # checkbox
        home_page.mark_checkbox().click()

        # clicking radio button
        home_page.mark_radio_button().click()

        # static dropdown
        self.select_option_by_visible_text(home_page.select_gender_dropdown(), get_data["gender"])   # called function in BaseClass to make the code cleaner

        # dropdown.select_by_index(1) #select female
        # dropdown.select_by_value("<value>")

        # create a custom xpath for any element
        # //tagname[@attribute='value'] -> ex. //input[@type='submit']

        # clicking submit button
        home_page.submit_form().click()

        # validating message
        message = home_page.validate_message().text
        assert 'Success' in message

        #refresh the page after finishing the 1st set
        self.driver.refresh()

    # used fixture here instead of putting it in conftest since this can't be used across multiple testcase
    @pytest.fixture(params=HomePageData.get_test_data("Testcase2"))
    def get_data(self, request):
        return request.param
