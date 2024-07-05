import pytest
from src.services.post_service import PostService
from src.config.logging_config import configure_logging, get_logger

# Configure logging
configure_logging()
logger = get_logger(__name__)


class TestPostsAPI:
    """
    Test class for Posts API.
    Encapsulates test cases for the Posts endpoints.
    """

    @classmethod
    def setup_class(cls):
        """
        Setup for the entire test class.
        Initializes the PostService.
        """
        cls.post_service = PostService()
        logger.info("Initialized PostService for test class.")

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

    def test_get_posts(self):
        """
        Test to get all posts and verify the response.
        """
        try:
            response = self.post_service.fetch_all_posts()
            assert len(response) > 0
            logger.info("test_get_posts passed.")
        except Exception as e:
            logger.error(f"test_get_posts failed: {e}")
            pytest.fail(f"Get posts failed: {e}")

    def test_get_post_by_id(self):
        """
        Test to get a post by ID and verify the response.
        """
        post_id = 1
        try:
            response = self.post_service.fetch_post_by_id(post_id)
            assert response['id'] == post_id
            logger.info("test_get_post_by_id passed.")
        except Exception as e:
            logger.error(f"test_get_post_by_id failed: {e}")
            pytest.fail(f"Get post by ID failed: {e}")

    def test_create_post(self):
        """
        Test to create a new post and verify the response.
        """
        new_post = {
            'title': 'foo',
            'body': 'bar',
            'userId': 1
        }
        try:
            response = self.post_service.create_post(new_post)
            assert response['title'] == new_post['title']
            logger.info("test_create_post passed.")
        except Exception as e:
            logger.error(f"test_create_post failed: {e}")
            pytest.fail(f"Create post failed: {e}")

    def test_update_post(self):
        """
        Test to update a post and verify the response.
        """
        post_id = 1
        updated_post = {
            'id': post_id,
            'title': 'updated title',
            'body': 'updated body',
            'userId': 1
        }
        try:
            response = self.post_service.update_post(post_id, updated_post)
            assert response['title'] == updated_post['title']
            logger.info("test_update_post passed.")
        except Exception as e:
            logger.error(f"test_update_post failed: {e}")
            pytest.fail(f"Update post failed: {e}")

    def test_delete_post(self):
        """
        Test to delete a post and verify the response.
        """
        post_id = 1
        try:
            response = self.post_service.delete_post(post_id)
            assert response == 200
            logger.info("test_delete_post passed.")
        except Exception as e:
            logger.error(f"test_delete_post failed: {e}")
            pytest.fail(f"Delete post failed: {e}")
