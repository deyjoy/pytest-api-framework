import pytest
from src.services.photo_service import PhotoService
from src.config.logging_config import configure_logging, get_logger
from datetime import datetime

# Configure logging with a unique log file for this test run
log_file = f'logs/test_photos_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
configure_logging(log_file)
logger = get_logger(__name__)


class TestPhotosAPI:
    """
    Test class for Photos API.
    Encapsulates test cases for the Photos endpoints.
    """

    @classmethod
    def setup_class(cls):
        """
        Setup for the entire test class.
        Initializes the PhotoService.
        """
        cls.photo_service = PhotoService()
        logger.info("Initialized PhotoService for test class.")

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

    def test_get_photos(self):
        """
        Test to get all photos and verify the response.
        """
        try:
            response = self.photo_service.fetch_all_photos()
            assert len(response) > 0
            logger.info("test_get_photos passed.")
        except Exception as e:
            logger.error(f"test_get_photos failed: {e}")
            pytest.fail(f"Get photos failed: {e}")

    def test_get_photo_by_id(self):
        """
        Test to get a photo by ID and verify the response.
        """
        photo_id = 1
        try:
            response = self.photo_service.fetch_photo_by_id(photo_id)
            assert response['id'] == photo_id
            logger.info("test_get_photo_by_id passed.")
        except Exception as e:
            logger.error(f"test_get_photo_by_id failed: {e}")
            pytest.fail(f"Get photo by ID failed: {e}")

    def test_create_photo(self):
        """
        Test to create a new photo and verify the response.
        """
        new_photo = {
            'title': 'foo',
            'url': 'http://example.com/foo.jpg',
            'thumbnailUrl': 'http://example.com/foo_thumb.jpg',
            'albumId': 1
        }
        try:
            response = self.photo_service.create_photo(new_photo)
            assert response['title'] == new_photo['title']
            logger.info("test_create_photo passed.")
        except Exception as e:
            logger.error(f"test_create_photo failed: {e}")
            pytest.fail(f"Create photo failed: {e}")

    def test_update_photo(self):
        """
        Test to update a photo and verify the response.
        """
        photo_id = 1
        updated_photo = {
            'id': photo_id,
            'title': 'updated title',
            'url': 'http://example.com/updated.jpg',
            'thumbnailUrl': 'http://example.com/updated_thumb.jpg',
            'albumId': 1
        }
        try:
            response = self.photo_service.update_photo(photo_id, updated_photo)
            assert response['title'] == updated_photo['title']
            logger.info("test_update_photo passed.")
        except Exception as e:
            logger.error(f"test_update_photo failed: {e}")
            pytest.fail(f"Update photo failed: {e}")

    def test_delete_photo(self):
        """
        Test to delete a photo and verify the response.
        """
        photo_id = 1
        try:
            response = self.photo_service.delete_photo(photo_id)
            assert response == 200
            logger.info("test_delete_photo passed.")
        except Exception as e:
            logger.error(f"test_delete_photo failed: {e}")
            pytest.fail(f"Delete photo failed: {e}")
