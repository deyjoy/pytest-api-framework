from src.api.clients import APIClient
from src.utils.logging_config import configure_logging, get_logger

# Configure logging with a unique log file for this service
configure_logging()
logger = get_logger(__name__)


class CommentService:
    """
    Service class for Comments API.
    Provides high-level operations using the APIClient.
    """

    def __init__(self):
        self.client = APIClient()

    def fetch_all_comments(self):
        """
        Fetch all comments.

        :return: List of comments
        :rtype: list
        """
        try:
            response = self.client.get('comments')
            logger.info("Fetched all comments successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch all comments: {e}")
            raise Exception(f"Failed to fetch all comments: {e}")

    def fetch_comment_by_id(self, comment_id):
        """
        Fetch a single comment by ID.

        :param comment_id: ID of the comment
        :type comment_id: int
        :return: Comment data
        :rtype: dict
        """
        try:
            response = self.client.get(f'comments/{comment_id}')
            logger.info(f"Fetched comment by ID {comment_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch comment by ID {comment_id}: {e}")
            raise Exception(f"Failed to fetch comment by ID {comment_id}: {e}")

    def create_comment(self, new_comment):
        """
        Create a new comment.

        :param new_comment: Data for the new comment
        :type new_comment: dict
        :return: Created comment data
        :rtype: dict
        """
        try:
            response = self.client.post('comments', new_comment)
            logger.info(f"Created new comment successfully: {new_comment}")
            return response
        except Exception as e:
            logger.error(f"Failed to create comment: {e}")
            raise Exception(f"Failed to create comment: {e}")

    def update_comment(self, comment_id, updated_comment):
        """
        Update an existing comment.

        :param comment_id: ID of the comment to update
        :type comment_id: int
        :param updated_comment: Updated data for the comment
        :type updated_comment: dict
        :return: Updated comment data
        :rtype: dict
        """
        try:
            response = self.client.put(f'comments/{comment_id}', updated_comment)
            logger.info(f"Updated comment with ID {comment_id} successfully: {updated_comment}")
            return response
        except Exception as e:
            logger.error(f"Failed to update comment with ID {comment_id}: {e}")
            raise Exception(f"Failed to update comment with ID {comment_id}: {e}")

    def delete_comment(self, comment_id):
        """
        Delete a comment by ID.

        :param comment_id: ID of the comment to delete
        :type comment_id: int
        :return: HTTP status code
        :rtype: int
        """
        try:
            response = self.client.delete(f'comments/{comment_id}')
            logger.info(f"Deleted comment with ID {comment_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to delete comment with ID {comment_id}: {e}")
            raise Exception(f"Failed to delete comment with ID {comment_id}: {e}")
