import pytest
import json
import os
from src.services.photo_service import PhotoService
from src.utils.logging_utils import setup_logging


@pytest.fixture(scope='class')
def photo_service():
    service = PhotoService()
    logger = setup_logging('photos')
    logger.info("Initialized PhotoService for test class.")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(base_dir, '../data/photos_test_data.json')
    with open(data_file) as f:
        test_data = json.load(f)
    return service, logger, test_data


class TestPhotosAPI:
    """
    Test class for Photos API.
    Encapsulates test cases for the Photos endpoints.
    """

    def test_get_photos(self, photo_service):
        """
        Test to get all photos and verify the response.
        """
        photo_service, logger, test_data = photo_service
        try:
            response = photo_service.fetch_all_photos()
            assert len(response) > 0
            logger.info("test_get_photos passed.")
        except Exception as e:
            logger.error(f"test_get_photos failed: {e}")
            pytest.fail(f"Get photos failed: {e}")

    def test_get_photo_by_id(self, photo_service):
        """
        Test to get a photo by ID and verify the response.
        """
        photo_service, logger, test_data = photo_service
        photo_id = test_data["get_photo_by_id"]["photo_id"]
        try:
            response = photo_service.fetch_photo_by_id(photo_id)
            assert response['id'] == photo_id
            logger.info("test_get_photo_by_id passed.")
        except Exception as e:
            logger.error(f"test_get_photo_by_id failed: {e}")
            pytest.fail(f"Get photo by ID failed: {e}")

    def test_create_photo(self, photo_service):
        """
        Test to create a new photo and verify the response.
        """
        photo_service, logger, test_data = photo_service
        new_photo = test_data["create_photo"]["new_photo"]
        try:
            response = photo_service.create_photo(new_photo)
            assert response['title'] == new_photo['title']
            logger.info("test_create_photo passed.")
        except Exception as e:
            logger.error(f"test_create_photo failed: {e}")
            pytest.fail(f"Create photo failed: {e}")

    def test_update_photo(self, photo_service):
        """
        Test to update a photo and verify the response.
        """
        photo_service, logger, test_data = photo_service
        photo_id = test_data["update_photo"]["photo_id"]
        updated_photo = test_data["update_photo"]["updated_photo"]
        try:
            response = photo_service.update_photo(photo_id, updated_photo)
            assert response['title'] == updated_photo['title']
            logger.info("test_update_photo passed.")
        except Exception as e:
            logger.error(f"test_update_photo failed: {e}")
            pytest.fail(f"Update photo failed: {e}")

    def test_delete_photo(self, photo_service):
        """
        Test to delete a photo and verify the response.
        """
        photo_service, logger, test_data = photo_service
        photo_id = test_data["delete_photo"]["photo_id"]
        try:
            response = photo_service.delete_photo(photo_id)
            assert response == 200
            logger.info("test_delete_photo passed.")
        except Exception as e:
            logger.error(f"test_delete_photo failed: {e}")
            pytest.fail(f"Delete photo failed: {e}")
