from src.api.clients import APIClient
from src.utils.logging_config import configure_logging, get_logger

# Configure logging with a unique log file for this service
configure_logging()
logger = get_logger(__name__)


class UserService:
    """
    Service class for Users API.
    Provides high-level operations using the APIClient.
    """

    def __init__(self):
        self.client = APIClient()

    def fetch_all_users(self):
        """
        Fetch all users.

        :return: List of users
        :rtype: list
        """
        try:
            response = self.client.get('users')
            logger.info("Fetched all users successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch all users: {e}")
            raise Exception(f"Failed to fetch all users: {e}")

    def fetch_user_by_id(self, user_id):
        """
        Fetch a single user by ID.

        :param user_id: ID of the user
        :type user_id: int
        :return: User data
        :rtype: dict
        """
        try:
            response = self.client.get(f'users/{user_id}')
            logger.info(f"Fetched user by ID {user_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch user by ID {user_id}: {e}")
            raise Exception(f"Failed to fetch user by ID {user_id}: {e}")

    def create_user(self, new_user):
        """
        Create a new user.

        :param new_user: Data for the new user
        :type new_user: dict
        :return: Created user data
        :rtype: dict
        """
        try:
            response = self.client.post('users', new_user)
            logger.info(f"Created new user successfully: {new_user}")
            return response
        except Exception as e:
            logger.error(f"Failed to create user: {e}")
            raise Exception(f"Failed to create user: {e}")

    def update_user(self, user_id, updated_user):
        """
        Update an existing user.

        :param user_id: ID of the user to update
        :type user_id: int
        :param updated_user: Updated data for the user
        :type updated_user: dict
        :return: Updated user data
        :rtype: dict
        """
        try:
            response = self.client.put(f'users/{user_id}', updated_user)
            logger.info(f"Updated user with ID {user_id} successfully: {updated_user}")
            return response
        except Exception as e:
            logger.error(f"Failed to update user with ID {user_id}: {e}")
            raise Exception(f"Failed to update user with ID {user_id}: {e}")

    def delete_user(self, user_id):
        """
        Delete a user by ID.

        :param user_id: ID of the user to delete
        :type user_id: int
        :return: HTTP status code
        :rtype: int
        """
        try:
            response = self.client.delete(f'users/{user_id}')
            logger.info(f"Deleted user with ID {user_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to delete user with ID {user_id}: {e}")
            raise Exception(f"Failed to delete user with ID {user_id}: {e}")
