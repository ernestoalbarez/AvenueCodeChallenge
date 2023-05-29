from ToDoApp.src.page_object.app_locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import string
import random


class MyTasksPage(object):
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_page(self):
        self.driver.find_element(
            By.CSS_SELECTOR,
            Locators.signin_page_button
        ).click()

    def enter_username(self, username):
        self.driver.find_element(
            By.ID,
            Locators.user_email
        ).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(
            By.ID,
            Locators.user_password
        ).send_keys(password)

    def login_user(self, username, password):
        self.navigate_to_login_page()
        self.enter_username(username)
        self.enter_password(password)

        self.driver.find_element(
            By.CSS_SELECTOR,
            Locators.user_signin_button
        ).click()

    def find_signed_in_success_message(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            Locators.signed_in_success_mesage
        ).is_displayed()

    def find_my_tasks_header(self):
        return self.driver.find_element(
            By.TAG_NAME,
            Locators.header_page
        ).is_displayed()

    def navigate_to_my_tasks_page(self):
        self.driver.find_element(
            By.ID,
            Locators.my_tasks_page
        ).click()

    @staticmethod
    def create_task_name(name_size):
        return ''.join(random.sample(string.ascii_uppercase, name_size))

    def create_task(self, task_name):
        task_input = self.driver.find_element(
            By.ID,
            Locators.new_task_input
        )
        task_input.send_keys(task_name)
        task_input.send_keys(Keys.ENTER)

    def find_task_by_name(self, task_name):
        return self.driver.find_element(
            By.XPATH,
            f'//a[contains(text(), "{task_name}")]'
        ).is_displayed()

    def delete_task(self, task):
        task_row = self.get_task_row_by_name(task)
        task_row.find_element(
            By.XPATH,
            Locators.remove_task_button
        ).click()

    def edit_task(self, task):
        self.driver.find_element(
            By.XPATH,
            f'//a[contains(text(), "{task}")]'
        ).click()

        name_input = self.driver.find_element(
            By.XPATH,
            Locators.row_task_input
        )
        name_input.send_keys(
            self.create_task_name(3)
        )
        name_input.send_keys(Keys.ENTER)

    def get_task_row_by_name(self, task):
        table_rows = self.driver.find_elements(
            By.XPATH,
            Locators.task_row
        )
        task_row = None

        for row in table_rows:
            if row.find_element(
                    By.XPATH,
                    f'//a[contains(text(), "{task}")]'
            ) is not None:
                task_row = row

        return task_row

    def find_manage_task_modal(self):
        return self.driver.find_element(
            By.CSS_SELECTOR,
            Locators.sub_task_modal
        ).is_displayed()

    def open_manage_task(self, task):
        task_row = self.get_task_row_by_name(task)
        task_row.find_element(
            By.XPATH,
            Locators.manage_task_button
        ).click()

    def create_sub_task(self, description):
        sub_task = self.driver.find_element(
            By.ID,
            Locators.new_sub_task_input
        )
        sub_task.send_keys(description)
        sub_task.send_keys(Keys.ENTER)

    def find_sub_task_by_name(self, description):
        modal = self.driver.find_element(
            By.CSS_SELECTOR,
            Locators.sub_task_modal
        )

        return modal.find_element(
            By.XPATH,
            f'//a[contains(text(), "{description}")]',
        ).is_displayed()

    def delete_sub_task(self):
        modal = self.driver.find_element(
            By.CSS_SELECTOR,
            Locators.sub_task_modal
        )
        modal.find_element(
            By.XPATH,
            Locators.remove_sub_task_button
        ).click()

    def edit_sub_task(self, task):
        modal = self.driver.find_element(
            By.CSS_SELECTOR,
            Locators.sub_task_modal
        )
        modal.find_element(
            By.XPATH,
            f'//a[contains(text(), "{task}")]'
        ).click()

        name_input = self.driver.find_element(
            By.XPATH,
            Locators.row_task_input
        )
        name_input.send_keys(
            self.create_task_name(5)
        )
        name_input.send_keys(Keys.ENTER)
