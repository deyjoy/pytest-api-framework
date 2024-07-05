import pytest
import json
import os
from src.services.album_service import AlbumService
from src.config.logging_config import configure_logging, get_logger
from datetime import datetime

# Configure logging with a unique log file for this test run
log_file = f'logs/test_albums_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
configure_logging(log_file)
logger = get_logger(__name__)


class TestAlbumsAPI:
    """
    Test class for Albums API.
    Encapsulates test cases for the Albums endpoints.
    """

    @classmethod
    def setup_class(cls):
        """
        Setup for the entire test class.
        Initializes the AlbumService.
        """
        cls.album_service = AlbumService()
        logger.info("Initialized AlbumService for test class.")
        base_dir = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(base_dir, '../data/albums_test_data.json')
        with open(data_file) as f:
            cls.test_data = json.load(f)

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

    def test_get_albums(self):
        """
        Test to get all albums and verify the response.
        """
        try:
            response = self.album_service.fetch_all_albums()
            assert len(response) > 0
            logger.info("test_get_albums passed.")
        except Exception as e:
            logger.error(f"test_get_albums failed: {e}")
            pytest.fail(f"Get albums failed: {e}")

    def test_get_album_by_id(self):
        """
        Test to get an album by ID and verify the response.
        """
        album_id = self.test_data["get_album_by_id"]["album_id"]
        try:
            response = self.album_service.fetch_album_by_id(album_id)
            assert response['id'] == album_id
            logger.info("test_get_album_by_id passed.")
        except Exception as e:
            logger.error(f"test_get_album_by_id failed: {e}")
            pytest.fail(f"Get album by ID failed: {e}")

    def test_create_album(self):
        """
        Test to create a new album and verify the response.
        """
        new_album = self.test_data["create_album"]["new_album"]
        try:
            response = self.album_service.create_album(new_album)
            assert response['title'] == new_album['title']
            logger.info("test_create_album passed.")
        except Exception as e:
            logger.error(f"test_create_album failed: {e}")
            pytest.fail(f"Create album failed: {e}")

    def test_update_album(self):
        """
        Test to update an album and verify the response.
        """
        album_id = self.test_data["update_album"]["album_id"]
        updated_album = self.test_data["update_album"]["updated_album"]
        try:
            response = self.album_service.update_album(album_id, updated_album)
            assert response['title'] == updated_album['title']
            logger.info("test_update_album passed.")
        except Exception as e:
            logger.error(f"test_update_album failed: {e}")
            pytest.fail(f"Update album failed: {e}")

    def test_delete_album(self):
        """
        Test to delete an album and verify the response.
        """
        album_id = self.test_data["delete_album"]["album_id"]
        try:
            response = self.album_service.delete_album(album_id)
            assert response == 200
            logger.info("test_delete_album passed.")
        except Exception as e:
            logger.error(f"test_delete_album failed: {e}")
            pytest.fail(f"Delete album failed: {e}")
