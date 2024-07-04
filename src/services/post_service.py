from src.api.clients import APIClient
from src.utils.logging_config import configure_logging, get_logger

# Configure logging
configure_logging()
logger = get_logger(__name__)


class PostService:
    """
    Service class for Posts API.
    Provides high-level operations using the APIClient.
    """

    def __init__(self):
        self.client = APIClient()

    def fetch_all_posts(self):
        """
        Fetch all posts.

        :return: List of posts
        :rtype: list
        """
        try:
            response = self.client.get('posts')
            logger.info("Fetched all posts successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch all posts: {e}")
            raise Exception(f"Failed to fetch all posts: {e}")

    def fetch_post_by_id(self, post_id):
        """
        Fetch a single post by ID.

        :param post_id: ID of the post
        :type post_id: int
        :return: Post data
        :rtype: dict
        """
        try:
            response = self.client.get(f'posts/{post_id}')
            logger.info(f"Fetched post by ID {post_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to fetch post by ID {post_id}: {e}")
            raise Exception(f"Failed to fetch post by ID {post_id}: {e}")

    def create_post(self, new_post):
        """
        Create a new post.

        :param new_post: Data for the new post
        :type new_post: dict
        :return: Created post data
        :rtype: dict
        """
        try:
            response = self.client.post('posts', new_post)
            logger.info(f"Created new post successfully: {new_post}")
            return response
        except Exception as e:
            logger.error(f"Failed to create post: {e}")
            raise Exception(f"Failed to create post: {e}")

    def update_post(self, post_id, updated_post):
        """
        Update an existing post.

        :param post_id: ID of the post to update
        :type post_id: int
        :param updated_post: Updated data for the post
        :type updated_post: dict
        :return: Updated post data
        :rtype: dict
        """
        try:
            response = self.client.put(f'posts/{post_id}', updated_post)
            logger.info(f"Updated post with ID {post_id} successfully: {updated_post}")
            return response
        except Exception as e:
            logger.error(f"Failed to update post with ID {post_id}: {e}")
            raise Exception(f"Failed to update post with ID {post_id}: {e}")

    def delete_post(self, post_id):
        """
        Delete a post by ID.

        :param post_id: ID of the post to delete
        :type post_id: int
        :return: HTTP status code
        :rtype: int
        """
        try:
            response = self.client.delete(f'posts/{post_id}')
            logger.info(f"Deleted post with ID {post_id} successfully.")
            return response
        except Exception as e:
            logger.error(f"Failed to delete post with ID {post_id}: {e}")
            raise Exception(f"Failed to delete post with ID {post_id}: {e}")
