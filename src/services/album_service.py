from src.api.clients import APIClient
from src.utils.logging_config import configure_logging, get_logger

# Configure logging with a unique log file for this service
configure_logging()
logger = get_logger(__name__)


class AlbumService:
    """
    Service class for Albums API.
    Provides high-level operations using the APIClient.
    """

    def __init__(self):
        self.client = APIClient()

    def fetch_all_albums(self):
        """
        Fetch all albums.

        :return: List of albums
        :rtype: list
        """
        try:
            response = self.client.get('albums')
            logger.info("Fetched all albums successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch all albums: {e}")
            raise Exception(f"Failed to fetch all albums: {e}")

    def fetch_album_by_id(self, album_id):
        """
        Fetch a single album by ID.

        :param album_id: ID of the album
        :type album_id: int
        :return: Album data
        :rtype: dict
        """
        try:
            response = self.client.get(f'albums/{album_id}')
            logger.info(f"Fetched album by ID {album_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch album by ID {album_id}: {e}")
            raise Exception(f"Failed to fetch album by ID {album_id}: {e}")

    def create_album(self, new_album):
        """
        Create a new album.

        :param new_album: Data for the new album
        :type new_album: dict
        :return: Created album data
        :rtype: dict
        """
        try:
            response = self.client.post('albums', new_album)
            logger.info(f"Created new album successfully: {new_album}")
            return response
        except Exception as e:
            logger.error(f"Failed to create album: {e}")
            raise Exception(f"Failed to create album: {e}")

    def update_album(self, album_id, updated_album):
        """
        Update an existing album.

        :param album_id: ID of the album to update
        :type album_id: int
        :param updated_album: Updated data for the album
        :type updated_album: dict
        :return: Updated album data
        :rtype: dict
        """
        try:
            response = self.client.put(f'albums/{album_id}', updated_album)
            logger.info(f"Updated album with ID {album_id} successfully: {updated_album}")
            return response
        except Exception as e:
            logger.error(f"Failed to update album with ID {album_id}: {e}")
            raise Exception(f"Failed to update album with ID {album_id}: {e}")

    def delete_album(self, album_id):
        """
        Delete an album by ID.

        :param album_id: ID of the album to delete
        :type album_id: int
        :return: HTTP status code
        :rtype: int
        """
        try:
            response = self.client.delete(f'albums/{album_id}')
            logger.info(f"Deleted album with ID {album_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to delete album with ID {album_id}: {e}")
            raise Exception(f"Failed to delete album with ID {album_id}: {e}")
