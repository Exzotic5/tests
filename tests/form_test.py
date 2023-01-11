from pages.form_page import FormPage


class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/text-box')
        form_page.open()
        form_page.fill_field_and_submit()