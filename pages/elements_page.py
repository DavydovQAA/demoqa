import time
from base.base_class import Base

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class ElementsPage(Base):
    # Locators

    click_box_button_locators = "/html/body/div[2]/div/div/div[2]/div[1]/div/div/div[1]/div/ul/li[2]"
    home_button_locators = "//button[@aria-label='Toggle']"
    downloads_button_locators = "//*[@id='tree-node']/ol/li/ol/li[3]/span/button"
    word_file_locators = "//*[@id='tree-node']/ol/li/ol/li[3]/ol/li[1]/span/label"

    # Getters

    def get_button_click_box(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.click_box_button_locators)))

    def get_button_home(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.home_button_locators)))

    def get_button_downloads(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.downloads_button_locators)))

    def get_word_file(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.word_file_locators)))

        # Actions

    def click_button_click_box(self):
        self.get_button_click_box().click()
        print('Click button Click-box')

    def click_button_home(self):
        self.get_button_home().click()
        print('Click button Home')

    def click_button_downloads(self):
        self.get_button_downloads().click()
        print('Click button Downloads')

    def select_word_file(self):
        self.get_word_file().click()
        print('Select Word File.doc')

    # Methods

    def check_box_actions(self):
        self.click_button_click_box()
        self.click_button_home()
        self.click_button_downloads()
        self.select_word_file()
        time.sleep(2)
