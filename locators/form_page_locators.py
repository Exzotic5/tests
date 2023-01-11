from selenium.webdriver.common.by import By


class FormPageLocators:
    FULL_NAME = (By.ID, "userName")
    EMAIL = (By.ID, "userEmail")
    CURRENT_ADRESS = (By.ID, "currentAddress")
    PERMANENT_ADRESS = (By.ID, "permanentAddress")
