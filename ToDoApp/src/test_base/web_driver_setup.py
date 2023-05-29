import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from ToDoApp.src.page_object.app_locators import Locators
from ToDoApp.src.page_object.pages.my_tasks_page import MyTasksPage


class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

        self.driver.get(Locators.app_url)
        self.driver.set_page_load_timeout(30)

        self.my_tasks_page = MyTasksPage(self.driver)
        self.my_tasks_page.login_user(
            "ernesto.albarez@protonmail.com",
            "Qualityassurance"
        )

    def tearDown(self):
        if self.driver is not None:
            print("Cleanup of test environment")
            self.driver.close()
            self.driver.quit()
