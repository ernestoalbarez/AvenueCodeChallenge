from ToDoApp.src.test_base.web_driver_setup import WebDriverSetup
import unittest
from selenium.common import NoSuchElementException


class TestMyTasksPage(WebDriverSetup):
    def test_login_user(self):
        self.assertTrue(
            self.my_tasks_page.find_signed_in_success_message(),
            "Error - user was not signed in"
        )

    def test_create_task(self):
        self.my_tasks_page.navigate_to_my_tasks_page()

        task = self.my_tasks_page.create_task_name(3)
        self.my_tasks_page.create_task(task)

        self.assertTrue(
            self.my_tasks_page.find_task_by_name(task),
            "Error - task not found"
        )

    def test_delete_task(self):
        self.my_tasks_page.navigate_to_my_tasks_page()

        task = self.my_tasks_page.create_task_name(3)
        self.my_tasks_page.create_task(task)
        self.my_tasks_page.delete_task(task)

        try:
            self.my_tasks_page.find_task_by_name(task)
        except NoSuchElementException:
            pass

    def test_edit_task(self):
        self.my_tasks_page.navigate_to_my_tasks_page()

        task = self.my_tasks_page.create_task_name(3)
        self.my_tasks_page.create_task(task)
        self.my_tasks_page.edit_task(task)

        try:
            self.my_tasks_page.find_task_by_name(task)
        except NoSuchElementException:
            pass

    def test_open_manage_task(self):
        self.my_tasks_page.navigate_to_my_tasks_page()

        task = self.my_tasks_page.create_task_name(3)
        self.my_tasks_page.create_task(task)
        self.my_tasks_page.open_manage_task(task)

        self.assertTrue(
            self.my_tasks_page.find_manage_task_modal(),
            "Error - Cannot open Manage Subtasks modal"
        )

    def test_create_sbu_task(self):
        self.my_tasks_page.navigate_to_my_tasks_page()

        task = self.my_tasks_page.create_task_name(3)
        self.my_tasks_page.create_task(task)
        self.my_tasks_page.open_manage_task(task)

        task = self.my_tasks_page.create_task_name(5)
        self.my_tasks_page.create_sub_task(task)

        self.assertTrue(
            self.my_tasks_page.find_sub_task_by_name(task),
            "Error - task not found"
        )

    def test_edit_sub_task(self):
        self.my_tasks_page.navigate_to_my_tasks_page()

        task = self.my_tasks_page.create_task_name(3)
        self.my_tasks_page.create_task(task)
        self.my_tasks_page.open_manage_task(task)

        task = self.my_tasks_page.create_task_name(5)
        self.my_tasks_page.create_sub_task(task)
        self.my_tasks_page.edit_sub_task(task)

        try:
            self.my_tasks_page.find_sub_task_by_name(task)
        except NoSuchElementException:
            pass

    def test_delete_sub_task(self):
        self.my_tasks_page.navigate_to_my_tasks_page()

        task = self.my_tasks_page.create_task_name(3)
        self.my_tasks_page.create_task(task)
        self.my_tasks_page.open_manage_task(task)

        task = self.my_tasks_page.create_task_name(5)
        self.my_tasks_page.create_sub_task(task)
        self.my_tasks_page.delete_sub_task()

        try:
            self.my_tasks_page.find_sub_task_by_name(task)
        except NoSuchElementException:
            pass

    if __name__ == '__main__':
        unittest.main()
