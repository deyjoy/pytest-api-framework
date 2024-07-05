import pytest
from src.services.todo_service import TodoService
from src.config.logging_config import configure_logging, get_logger
from datetime import datetime

# Configure logging with a unique log file for this test run
log_file = f'logs/test_todos_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
configure_logging(log_file)
logger = get_logger(__name__)


class TestTodosAPI:
    """
    Test class for Todos API.
    Encapsulates test cases for the Todos endpoints.
    """

    @classmethod
    def setup_class(cls):
        """
        Setup for the entire test class.
        Initializes the TodoService.
        """
        cls.todo_service = TodoService()
        logger.info("Initialized TodoService for test class.")

    def setup_method(self):
        """
        Setup for each test method.
        """
        pass

    def teardown_method(self):
        """
        Teardown for each test method.
        """
        pass

    def test_get_todos(self):
        """
        Test to get all todos and verify the response.
        """
        try:
            response = self.todo_service.fetch_all_todos()
            assert len(response) > 0
            logger.info("test_get_todos passed.")
        except Exception as e:
            logger.error(f"test_get_todos failed: {e}")
            pytest.fail(f"Get todos failed: {e}")

    def test_get_todo_by_id(self):
        """
        Test to get a todo by ID and verify the response.
        """
        todo_id = 1
        try:
            response = self.todo_service.fetch_todo_by_id(todo_id)
            assert response['id'] == todo_id
            logger.info("test_get_todo_by_id passed.")
        except Exception as e:
            logger.error(f"test_get_todo_by_id failed: {e}")
            pytest.fail(f"Get todo by ID failed: {e}")

    def test_create_todo(self):
        """
        Test to create a new todo and verify the response.
        """
        new_todo = {
            'title': 'foo',
            'completed': False,
            'userId': 1
        }
        try:
            response = self.todo_service.create_todo(new_todo)
            assert response['title'] == new_todo['title']
            logger.info("test_create_todo passed.")
        except Exception as e:
            logger.error(f"test_create_todo failed: {e}")
            pytest.fail(f"Create todo failed: {e}")

    def test_update_todo(self):
        """
        Test to update a todo and verify the response.
        """
        todo_id = 1
        updated_todo = {
            'id': todo_id,
            'title': 'updated title',
            'completed': True,
            'userId': 1
        }
        try:
            response = self.todo_service.update_todo(todo_id, updated_todo)
            assert response['title'] == updated_todo['title']
            logger.info("test_update_todo passed.")
        except Exception as e:
            logger.error(f"test_update_todo failed: {e}")
            pytest.fail(f"Update todo failed: {e}")

    def test_delete_todo(self):
        """
        Test to delete a todo and verify the response.
        """
        todo_id = 1
        try:
            response = self.todo_service.delete_todo(todo_id)
            assert response == 200
            logger.info("test_delete_todo passed.")
        except Exception as e:
            logger.error(f"test_delete_todo failed: {e}")
            pytest.fail(f"Delete todo failed: {e}")
