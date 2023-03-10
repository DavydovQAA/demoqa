import time

from conftest import driver
from pages.elements_page import ElementsPage

from pages.main_page import MainPage


class TestSimple:

    def test_click_elements(self):
        mp = MainPage(driver)
        mp.click_elements()

        ep = ElementsPage(driver)
        ep.check_box_actions()
        time.sleep(2)  # debug sleep
