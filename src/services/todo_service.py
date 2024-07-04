from src.api.clients import APIClient
from src.utils.logging_config import configure_logging, get_logger

# Configure logging with a unique log file for this service
configure_logging()
logger = get_logger(__name__)


class TodoService:
    """
    Service class for Todos API.
    Provides high-level operations using the APIClient.
    """

    def __init__(self):
        self.client = APIClient()

    def fetch_all_todos(self):
        """
        Fetch all todos.

        :return: List of todos
        :rtype: list
        """
        try:
            response = self.client.get('todos')
            logger.info("Fetched all todos successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch all todos: {e}")
            raise Exception(f"Failed to fetch all todos: {e}")

    def fetch_todo_by_id(self, todo_id):
        """
        Fetch a single todo by ID.

        :param todo_id: ID of the todo
        :type todo_id: int
        :return: Todo data
        :rtype: dict
        """
        try:
            response = self.client.get(f'todos/{todo_id}')
            logger.info(f"Fetched todo by ID {todo_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch todo by ID {todo_id}: {e}")
            raise Exception(f"Failed to fetch todo by ID {todo_id}: {e}")

    def create_todo(self, new_todo):
        """
        Create a new todo.

        :param new_todo: Data for the new todo
        :type new_todo: dict
        :return: Created todo data
        :rtype: dict
        """
        try:
            response = self.client.post('todos', new_todo)
            logger.info(f"Created new todo successfully: {new_todo}")
            return response
        except Exception as e:
            logger.error(f"Failed to create todo: {e}")
            raise Exception(f"Failed to create todo: {e}")

    def update_todo(self, todo_id, updated_todo):
        """
        Update an existing todo.

        :param todo_id: ID of the todo to update
        :type todo_id: int
        :param updated_todo: Updated data for the todo
        :type updated_todo: dict
        :return: Updated todo data
        :rtype: dict
        """
        try:
            response = self.client.put(f'todos/{todo_id}', updated_todo)
            logger.info(f"Updated todo with ID {todo_id} successfully: {updated_todo}")
            return response
        except Exception as e:
            logger.error(f"Failed to update todo with ID {todo_id}: {e}")
            raise Exception(f"Failed to update todo with ID {todo_id}: {e}")

    def delete_todo(self, todo_id):
        """
        Delete a todo by ID.

        :param todo_id: ID of the todo to delete
        :type todo_id: int
        :return: HTTP status code
        :rtype: int
        """
        try:
            response = self.client.delete(f'todos/{todo_id}')
            logger.info(f"Deleted todo with ID {todo_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to delete todo with ID {todo_id}: {e}")
            raise Exception(f"Failed to delete todo with ID {todo_id}: {e}")
