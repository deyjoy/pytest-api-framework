import pytest
import json
import os
from src.services.user_service import UserService
from src.utils.logging_utils import setup_logging


@pytest.fixture(scope='class')
def user_service():
    service = UserService()
    logger = setup_logging('users')
    logger.info("Initialized UserService for test class.")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(base_dir, '../data/users_test_data.json')
    with open(data_file) as f:
        test_data = json.load(f)
    return service, logger, test_data


class TestUsersAPI:
    """
    Test class for Users API.
    Encapsulates test cases for the Users endpoints.
    """

    def test_get_users(self, user_service):
        """
        Test to get all users and verify the response.
        """
        user_service, logger, test_data = user_service
        try:
            response = user_service.fetch_all_users()
            assert len(response) > 0
            logger.info("test_get_users passed.")
        except Exception as e:
            logger.error(f"test_get_users failed: {e}")
            pytest.fail(f"Get users failed: {e}")

    def test_get_user_by_id(self, user_service):
        """
        Test to get a user by ID and verify the response.
        """
        user_service, logger, test_data = user_service
        user_id = test_data["get_user_by_id"]["user_id"]
        try:
            response = user_service.fetch_user_by_id(user_id)
            assert response['id'] == user_id
            logger.info("test_get_user_by_id passed.")
        except Exception as e:
            logger.error(f"test_get_user_by_id failed: {e}")
            pytest.fail(f"Get user by ID failed: {e}")

    def test_create_user(self, user_service):
        """
        Test to create a new user and verify the response.
        """
        user_service, logger, test_data = user_service
        new_user = test_data["create_user"]["new_user"]
        try:
            response = user_service.create_user(new_user)
            assert response['name'] == new_user['name']
            logger.info("test_create_user passed.")
        except Exception as e:
            logger.error(f"test_create_user failed: {e}")
            pytest.fail(f"Create user failed: {e}")

    def test_update_user(self, user_service):
        """
        Test to update a user and verify the response.
        """
        user_service, logger, test_data = user_service
        user_id = test_data["update_user"]["user_id"]
        updated_user = test_data["update_user"]["updated_user"]
        try:
            response = user_service.update_user(user_id, updated_user)
            assert response['name'] == updated_user['name']
            logger.info("test_update_user passed.")
        except Exception as e:
            logger.error(f"test_update_user failed: {e}")
            pytest.fail(f"Update user failed: {e}")

    def test_delete_user(self, user_service):
        """
        Test to delete a user and verify the response.
        """
        user_service, logger, test_data = user_service
        user_id = test_data["delete_user"]["user_id"]
        try:
            response = user_service.delete_user(user_id)
            assert response == 200
            logger.info("test_delete_user passed.")
        except Exception as e:
            logger.error(f"test_delete_user failed: {e}")
            pytest.fail(f"Delete user failed: {e}")
