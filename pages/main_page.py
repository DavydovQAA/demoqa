import time
from base.base_class import Base

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(Base):
    url = 'https://demoqa.com/'

    # Locators

    elements_button_locators = "//div[@class='card-up']"

    # Getters

    def get_button_elements(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.elements_button_locators)))

    # Actions

    def click_button_elements(self):
        self.get_button_elements().click()
        print('Click Elements')

    # Methods

    def click_elements(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_button_elements()
        time.sleep(2)
