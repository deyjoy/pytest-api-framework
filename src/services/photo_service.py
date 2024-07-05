from src.api.clients import APIClient
from src.config.logging_config import configure_logging, get_logger

# Configure logging with a unique log file for this service
configure_logging()
logger = get_logger(__name__)


class PhotoService:
    """
    Service class for Photos API.
    Provides high-level operations using the APIClient.
    """

    def __init__(self):
        self.client = APIClient()

    def fetch_all_photos(self):
        """
        Fetch all photos.

        :return: List of photos
        :rtype: list
        """
        try:
            response = self.client.get('photos')
            logger.info("Fetched all photos successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch all photos: {e}")
            raise Exception(f"Failed to fetch all photos: {e}")

    def fetch_photo_by_id(self, photo_id):
        """
        Fetch a single photo by ID.

        :param photo_id: ID of the photo
        :type photo_id: int
        :return: Photo data
        :rtype: dict
        """
        try:
            response = self.client.get(f'photos/{photo_id}')
            logger.info(f"Fetched photo by ID {photo_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch photo by ID {photo_id}: {e}")
            raise Exception(f"Failed to fetch photo by ID {photo_id}: {e}")

    def create_photo(self, new_photo):
        """
        Create a new photo.

        :param new_photo: Data for the new photo
        :type new_photo: dict
        :return: Created photo data
        :rtype: dict
        """
        try:
            response = self.client.post('photos', new_photo)
            logger.info(f"Created new photo successfully: {new_photo}")
            return response
        except Exception as e:
            logger.error(f"Failed to create photo: {e}")
            raise Exception(f"Failed to create photo: {e}")

    def update_photo(self, photo_id, updated_photo):
        """
        Update an existing photo.

        :param photo_id: ID of the photo to update
        :type photo_id: int
        :param updated_photo: Updated data for the photo
        :type updated_photo: dict
        :return: Updated photo data
        :rtype: dict
        """
        try:
            response = self.client.put(f'photos/{photo_id}', updated_photo)
            logger.info(f"Updated photo with ID {photo_id} successfully: {updated_photo}")
            return response
        except Exception as e:
            logger.error(f"Failed to update photo with ID {photo_id}: {e}")
            raise Exception(f"Failed to update photo with ID {photo_id}: {e}")

    def delete_photo(self, photo_id):
        """
        Delete a photo by ID.

        :param photo_id: ID of the photo to delete
        :type photo_id: int
        :return: HTTP status code
        :rtype: int
        """
        try:
            response = self.client.delete(f'photos/{photo_id}')
            logger.info(f"Deleted photo with ID {photo_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to delete photo with ID {photo_id}: {e}")
            raise Exception(f"Failed to delete photo with ID {photo_id}: {e}")
