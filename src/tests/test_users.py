import pytest
from src.services.user_service import UserService
from src.config.logging_config import configure_logging, get_logger
from datetime import datetime

# Configure logging with a unique log file for this test run
log_file = f'logs/test_users_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
configure_logging(log_file)
logger = get_logger(__name__)


class TestUsersAPI:
    """
    Test class for Users API.
    Encapsulates test cases for the Users endpoints.
    """

    @classmethod
    def setup_class(cls):
        """
        Setup for the entire test class.
        Initializes the UserService.
        """
        cls.user_service = UserService()
        logger.info("Initialized UserService for test class.")

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

    def test_get_users(self):
        """
        Test to get all users and verify the response.
        """
        try:
            response = self.user_service.fetch_all_users()
            assert len(response) > 0
            logger.info("test_get_users passed.")
        except Exception as e:
            logger.error(f"test_get_users failed: {e}")
            pytest.fail(f"Get users failed: {e}")

    def test_get_user_by_id(self):
        """
        Test to get a user by ID and verify the response.
        """
        user_id = 1
        try:
            response = self.user_service.fetch_user_by_id(user_id)
            assert response['id'] == user_id
            logger.info("test_get_user_by_id passed.")
        except Exception as e:
            logger.error(f"test_get_user_by_id failed: {e}")
            pytest.fail(f"Get user by ID failed: {e}")

    def test_create_user(self):
        """
        Test to create a new user and verify the response.
        """
        new_user = {
            'name': 'foo',
            'username': 'bar',
            'email': 'foo@bar.com'
        }
        try:
            response = self.user_service.create_user(new_user)
            assert response['name'] == new_user['name']
            logger.info("test_create_user passed.")
        except Exception as e:
            logger.error(f"test_create_user failed: {e}")
            pytest.fail(f"Create user failed: {e}")

    def test_update_user(self):
        """
        Test to update a user and verify the response.
        """
        user_id = 1
        updated_user = {
            'id': user_id,
            'name': 'updated name',
            'username': 'updated username',
            'email': 'updated@bar.com'
        }
        try:
            response = self.user_service.update_user(user_id, updated_user)
            assert response['name'] == updated_user['name']
            logger.info("test_update_user passed.")
        except Exception as e:
            logger.error(f"test_update_user failed: {e}")
            pytest.fail(f"Update user failed: {e}")

    def test_delete_user(self):
        """
        Test to delete a user and verify the response.
        """
        user_id = 1
        try:
            response = self.user_service.delete_user(user_id)
            assert response == 200
            logger.info("test_delete_user passed.")
        except Exception as e:
            logger.error(f"test_delete_user failed: {e}")
            pytest.fail(f"Delete user failed: {e}")
