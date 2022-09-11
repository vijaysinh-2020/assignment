from calendar import c
import time
from unicodedata import category
from locator import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from element import BasePageElement
import re


class SearchFieldElement(BasePageElement):
    locator = HomePageLocators.SEARCH_FIELD[1]
    by = HomePageLocators.SEARCH_FIELD[0]


class BasePage(object):
    def __init__(self, driver) -> None:
        self.driver = driver
    

class HomePage(BasePage):
    search_field_element = SearchFieldElement()

    def is_title_matches(self):
        print(self.driver.title)
        return "My Store" == self.driver.title

    def click_on_women_category(self):
        top_menu = self.driver.find_element(*HomePageLocators.MAIN_MENU)
        link = top_menu.find_element(By.CSS_SELECTOR, "a.sf-with-ul[title=Women]")
        link.click()

    def add_to_cart(self):
        popular_section = self.driver.find_element(*HomePageLocators.POPULAR_SECTION)
        popular_section.find_element(By.CLASS_NAME, "ajax_add_to_cart_button").click()

    def is_product_added_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            lambda x: self.driver.execute_script("return jQuery.active == 0")
        )
        cart_modal = self.driver.find_element(*HomePageLocators.ADD_TO_CART_MODAL)
        t = cart_modal.find_element(By.CLASS_NAME, "ajax_cart_product_txt")
        return t.text == "There is 1 item in your cart."
    

class SearchResultPage(BasePage):


    def select_color(self):
        layered_form = self.driver.find_element(*SearchPageLocators.FILTER_FORM)
        color = layered_form.find_element(By.CSS_SELECTOR, "input.color-option")
        color.click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            lambda x: self.driver.execute_script("return jQuery.active == 0")
        )

    def select_category(self):
        layered_form = self.driver.find_element(*SearchPageLocators.FILTER_FORM)
        category = layered_form.find_element(By.CSS_SELECTOR, "#ul_layered_category_0 input[type=checkbox]")
        category.click()
        time.sleep(1)
        WebDriverWait(self.driver, 10).until(
            lambda x: self.driver.execute_script("return jQuery.active == 0")
        )

    def has_color_category_in_title(self):
        center_element = self.driver.find_element(*SearchPageLocators.CENTER_COLUMN)
        return 'WOMEN > CATEGORIES DRESSES > COLOR BEIGE' in center_element.find_element(By.CSS_SELECTOR, "h1.page-heading > .cat-name").text

    def no_results_found(self):
        center_element = self.driver.find_element(*SearchPageLocators.CENTER_COLUMN)
        return "No results were found for your search" in center_element.text

    def results_found(self):
        center_element = self.driver.find_element(*SearchPageLocators.CENTER_COLUMN)
        return bool(re.search(r"Showing .* - .* of .* item", center_element.text))