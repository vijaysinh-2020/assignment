from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import page
import time

DRIVER_PATH = "D:\\testing\\chromedriver.exe"

class StoreTest(unittest.TestCase):
    def setUp(self):
        ser = Service(DRIVER_PATH)
        op = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=ser, options=op)
        self.driver.get("http://automationpractice.com/index.php")
    
    def test_search_results(self):
        home_page = page.HomePage(self.driver)
        assert home_page.is_title_matches()
        home_page.search_field_element = "shirt"
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.results_found()

        home_page.search_field_element = "asdasdads"
        search_result_page = page.SearchResultPage(self.driver)
        assert search_result_page.no_results_found()

    def test_search_filters(self):
        home_page = page.HomePage(self.driver)
        home_page.click_on_women_category()
        search_result_page = page.SearchResultPage(self.driver)
        search_result_page.select_color()
        search_result_page.select_category()

        assert search_result_page.has_color_category_in_title()
        assert search_result_page.results_found()

    def test_add_to_cart(self):
        home_page = page.HomePage(self.driver)
        home_page.add_to_cart()
        assert home_page.is_product_added_to_cart()

    

    def tearDown(self) -> None:
        self.driver.close()

        

if __name__ == "__main__":
    unittest.main()
