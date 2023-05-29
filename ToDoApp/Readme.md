# Avenue Code Challenge
This is the given framework solution for the code challenge

## Set up
- Download and install [Python](https://www.python.org/downloads/)
- Install [Pytest](https://docs.pytest.org/en/6.2.x/getting-started.html)
- Create a python [virtual environment](https://docs.python.org/3/library/venv.html)

## Run tests
Simply run the file `ToDoApp/tests/test_suite/test_runner.py` which contains all tests configuration

### Tests
- **test_login_user**: assert whether the user was logged in or not
- **test_create_task**: creates a task and assert whether the tasks is listed or not
- **test_edit_task**: creates a new task, renames it and assert whether the old tasks name is listed or not
- **test_delete_task**: creates a new task, deletes it and assert whether the old tasks name is listed or not
- **test_open_manage_task**: creates a task, open the Manage Task modal and assert whether the modal is present or not
- **test_create_sbu_task**: creates a task, open the Manage Task modal, creates a sub-task and assert whether the tasks is listed or not
- **test_edit_sub_task** creates a task, open the Manage Task modal, creates a sub-task, renames it  and assert whether the tasks is listed or not
- **test_delete_sub_task** creates a task, open the Manage Task modal, creates a sub-task, deletes it  and assert whether the tasks is listed or not

## Bugs reported after manual testing
- Task must have at least 3 characters
- There is not message for top limit for task characters
- Message on top does not compile user story
- Sub-task can be created with no due date
- Sub-task can be created with no description
- Missing waring for 250 description for sub-task character limit