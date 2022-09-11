from selenium.webdriver.common.by import By
class HomePageLocators(object):
    SEARCH_FIELD = (By.ID, "search_query_top")
    MAIN_MENU = (By.ID, "block_top_menu")
    POPULAR_SECTION = (By.ID, "homefeatured")
    ADD_TO_CART_MODAL = (By.ID, "layer_cart")

class SearchPageLocators(object):
    CENTER_COLUMN = (By.ID, "center_column")
    FILTER_FORM = (By.ID, "layered_form")