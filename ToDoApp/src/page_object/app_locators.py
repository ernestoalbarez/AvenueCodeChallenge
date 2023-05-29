class Locators(object):
    app_url = "https://qa-test.avenuecode.io/"
    # landing page
    signin_page_button = ".btn.btn-lg.btn-primary"
    register_button = ".btn.btn-lg.btn-warning"
    # sign in page
    user_email = "user_email"
    user_password = "user_password"
    user_signin_button = ".btn.btn-primary"
    # to do list page
    signed_in_success_mesage = ".alert.alert-info"
    my_tasks_page = "my_task"
    header_page = "h1"
    new_task_input = "new_task"
    task_row = "//tbody/tr"
    row_task_input = "//td/form/div/input"
    task_description = '//td/a'
    manage_task_button = "// button[contains(text(), 'Manage Subtasks')]"
    remove_task_button = "// button[contains(text(), 'Remove')]"
    # sub-task pop-up
    sub_task_modal = ".modal-content"
    new_sub_task_input = "new_sub_task"
    remove_sub_task_button = "// button[contains(text(), 'Remove SubTask')]"
