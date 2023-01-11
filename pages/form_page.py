from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators

class FormPage(BasePage):

    def fill_field_and_submit(self):
        email = 'milo'
        full_name = 'makar4ik'
        current_adress = '123adress'
        permanent_adress = 'adress456'
        self.element_is_visible(Locators.EMAIL).send_keys(email)
        self.element_is_visible(Locators.FULL_NAME).send_keys(full_name)
        self.element_is_visible(Locators.CURRENT_ADRESS).send_keys(current_adress)
        self.element_is_visible(Locators.PERMANENT_ADRESS).send_keys(permanent_adress)
