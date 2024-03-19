from time import sleep

from selenium.webdriver.common.by import By

from pages.base_page import Page


class OffPlanPage(Page):

    OFF_PLAN_LINK = (By.CSS_SELECTOR, "[class='menu-twobutton']")
    ALL_PRODUCTS = (By.CSS_SELECTOR, "[wized='cardOfProperty']")
    OFF_PLAN_PROJECT_COUNTER = (By.CSS_SELECTOR, ".properties-counter")
    PROJECT_NAME = (By.CSS_SELECTOR, ".property-header-name-text")
    VISUALIZATION_TABS = (By.CSS_SELECTOR, "[id*='w-tabs-0-data-w-tab']")
    ARCHITECTURE_TAB = (By.CSS_SELECTOR, "[data-w-tab='Tab 1']")
    INTERIOR_TAB = (By.CSS_SELECTOR, "[data-w-tab='Tab 2']")
    LOBBY_TAB = (By.CSS_SELECTOR, "[data-w-tab='Tab 3']")

    def click_off_plan(self):
        self.click(*self.OFF_PLAN_LINK)

    def click_first_product(self):
        self.presence_of_element_located(*self.OFF_PLAN_PROJECT_COUNTER)
        # requires extra sleep to load the page.
        sleep(2)
        elements = self.find_elements(*self.ALL_PRODUCTS)[1].click()

    def verify_product_page_loaded(self):
        self.presence_of_element_located(*self.PROJECT_NAME)

    def verify_visualization(self):
        visualization_tab = ['Architecture', 'Interior', 'Lobby']
        tabs = self.find_elements(*self.VISUALIZATION_TABS)
        i = 0
        for tab in tabs:
            # print(tab.text)
            if tab.text in visualization_tab:
                i += 1

            assert tab.text in visualization_tab, f"'{visualization_tab[i]}' tab is not present under Visualization"

    def verify_visualization_options_clickable(self):
        # tabs = self.find_elements(*self.VISUALIZATION_TABS)
        # for tab in tabs:
        #     self.wait_element_clickable(*tab)

        self.wait_element_clickable(*self.ARCHITECTURE_TAB)
        self.wait_element_clickable(*self.INTERIOR_TAB)
        self.wait_element_clickable(*self.LOBBY_TAB)