import pytest
import json
import os
from src.services.todo_service import TodoService
from src.utils.logging_utils import setup_logging


@pytest.fixture(scope='class')
def todo_service():
    service = TodoService()
    logger = setup_logging('todos')
    logger.info("Initialized TodoService for test class.")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(base_dir, '../data/todos_test_data.json')
    with open(data_file) as f:
        test_data = json.load(f)
    return service, logger, test_data


class TestTodosAPI:
    """
    Test class for Todos API.
    Encapsulates test cases for the Todos endpoints.
    """

    def test_get_todos(self, todo_service):
        """
        Test to get all todos and verify the response.
        """
        todo_service, logger, test_data = todo_service
        try:
            response = todo_service.fetch_all_todos()
            assert len(response) > 0
            logger.info("test_get_todos passed.")
        except Exception as e:
            logger.error(f"test_get_todos failed: {e}")
            pytest.fail(f"Get todos failed: {e}")

    def test_get_todo_by_id(self, todo_service):
        """
        Test to get a todo by ID and verify the response.
        """
        todo_service, logger, test_data = todo_service
        todo_id = test_data["get_todo_by_id"]["todo_id"]
        try:
            response = todo_service.fetch_todo_by_id(todo_id)
            assert response['id'] == todo_id
            logger.info("test_get_todo_by_id passed.")
        except Exception as e:
            logger.error(f"test_get_todo_by_id failed: {e}")
            pytest.fail(f"Get todo by ID failed: {e}")

    def test_create_todo(self, todo_service):
        """
        Test to create a new todo and verify the response.
        """
        todo_service, logger, test_data = todo_service
        new_todo = test_data["create_todo"]["new_todo"]
        try:
            response = todo_service.create_todo(new_todo)
            assert response['title'] == new_todo['title']
            logger.info("test_create_todo passed.")
        except Exception as e:
            logger.error(f"test_create_todo failed: {e}")
            pytest.fail(f"Create todo failed: {e}")

    def test_update_todo(self, todo_service):
        """
        Test to update a todo and verify the response.
        """
        todo_service, logger, test_data = todo_service
        todo_id = test_data["update_todo"]["todo_id"]
        updated_todo = test_data["update_todo"]["updated_todo"]
        try:
            response = todo_service.update_todo(todo_id, updated_todo)
            assert response['title'] == updated_todo['title']
            logger.info("test_update_todo passed.")
        except Exception as e:
            logger.error(f"test_update_todo failed: {e}")
            pytest.fail(f"Update todo failed: {e}")

    def test_delete_todo(self, todo_service):
        """
        Test to delete a todo and verify the response.
        """
        todo_service, logger, test_data = todo_service
        todo_id = test_data["delete_todo"]["todo_id"]
        try:
            response = todo_service.delete_todo(todo_id)
            assert response == 200
            logger.info("test_delete_todo passed.")
        except Exception as e:
            logger.error(f"test_delete_todo failed: {e}")
            pytest.fail(f"Delete todo failed: {e}")
