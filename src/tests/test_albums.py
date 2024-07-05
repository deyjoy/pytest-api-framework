import pytest
import json
import os
from src.services.album_service import AlbumService
from src.utils.logging_utils import setup_logging


@pytest.fixture(scope='class')
def album_service():
    service = AlbumService()
    logger = setup_logging('albums')
    logger.info("Initialized AlbumService for test class.")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(base_dir, '../data/albums_test_data.json')
    with open(data_file) as f:
        test_data = json.load(f)
    return service, logger, test_data


class TestAlbumsAPI:
    """
    Test class for Albums API.
    Encapsulates test cases for the Albums endpoints.
    """

    def test_get_albums(self, album_service):
        """
        Test to get all albums and verify the response.
        """
        album_service, logger, test_data = album_service
        try:
            response = album_service.fetch_all_albums()
            assert len(response) > 0
            logger.info("test_get_albums passed.")
        except Exception as e:
            logger.error(f"test_get_albums failed: {e}")
            pytest.fail(f"Get albums failed: {e}")

    def test_get_album_by_id(self, album_service):
        """
        Test to get an album by ID and verify the response.
        """
        album_service, logger, test_data = album_service
        album_id = test_data["get_album_by_id"]["album_id"]
        try:
            response = album_service.fetch_album_by_id(album_id)
            assert response['id'] == album_id
            logger.info("test_get_album_by_id passed.")
        except Exception as e:
            logger.error(f"test_get_album_by_id failed: {e}")
            pytest.fail(f"Get album by ID failed: {e}")

    def test_create_album(self, album_service):
        """
        Test to create a new album and verify the response.
        """
        album_service, logger, test_data = album_service
        new_album = test_data["create_album"]["new_album"]
        try:
            response = album_service.create_album(new_album)
            assert response['title'] == new_album['title']
            logger.info("test_create_album passed.")
        except Exception as e:
            logger.error(f"test_create_album failed: {e}")
            pytest.fail(f"Create album failed: {e}")

    def test_update_album(self, album_service):
        """
        Test to update an album and verify the response.
        """
        album_service, logger, test_data = album_service
        album_id = test_data["update_album"]["album_id"]
        updated_album = test_data["update_album"]["updated_album"]
        try:
            response = album_service.update_album(album_id, updated_album)
            assert response['title'] == updated_album['title']
            logger.info("test_update_album passed.")
        except Exception as e:
            logger.error(f"test_update_album failed: {e}")
            pytest.fail(f"Update album failed: {e}")

    def test_delete_album(self, album_service):
        """
        Test to delete an album and verify the response.
        """
        album_service, logger, test_data = album_service
        album_id = test_data["delete_album"]["album_id"]
        try:
            response = album_service.delete_album(album_id)
            assert response == 200
            logger.info("test_delete_album passed.")
        except Exception as e:
            logger.error(f"test_delete_album failed: {e}")
            pytest.fail(f"Delete album failed: {e}")
