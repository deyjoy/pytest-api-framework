import pytest
import json
import os
from src.services.post_service import PostService
from src.utils.logging_utils import setup_logging


@pytest.fixture(scope='class')
def post_service():
    service = PostService()
    logger = setup_logging('posts')
    logger.info("Initialized PostService for test class.")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(base_dir, '../data/posts_test_data.json')
    with open(data_file) as f:
        test_data = json.load(f)
    return service, logger, test_data


class TestPostsAPI:
    """
    Test class for Posts API.
    Encapsulates test cases for the Posts endpoints.
    """

    def test_get_posts(self, post_service):
        """
        Test to get all posts and verify the response.
        """
        post_service, logger, test_data = post_service
        try:
            response = post_service.fetch_all_posts()
            assert len(response) > 0
            logger.info("test_get_posts passed.")
        except Exception as e:
            logger.error(f"test_get_posts failed: {e}")
            pytest.fail(f"Get posts failed: {e}")

    def test_get_post_by_id(self, post_service):
        """
        Test to get a post by ID and verify the response.
        """
        post_service, logger, test_data = post_service
        post_id = test_data["get_post_by_id"]["post_id"]
        try:
            response = post_service.fetch_post_by_id(post_id)
            assert response['id'] == post_id
            logger.info("test_get_post_by_id passed.")
        except Exception as e:
            logger.error(f"test_get_post_by_id failed: {e}")
            pytest.fail(f"Get post by ID failed: {e}")

    def test_create_post(self, post_service):
        """
        Test to create a new post and verify the response.
        """
        post_service, logger, test_data = post_service
        new_post = test_data["create_post"]["new_post"]
        try:
            response = post_service.create_post(new_post)
            assert response['title'] == new_post['title']
            logger.info("test_create_post passed.")
        except Exception as e:
            logger.error(f"test_create_post failed: {e}")
            pytest.fail(f"Create post failed: {e}")

    def test_update_post(self, post_service):
        """
        Test to update a post and verify the response.
        """
        post_service, logger, test_data = post_service
        post_id = test_data["update_post"]["post_id"]
        updated_post = test_data["update_post"]["updated_post"]
        try:
            response = post_service.update_post(post_id, updated_post)
            assert response['title'] == updated_post['title']
            logger.info("test_update_post passed.")
        except Exception as e:
            logger.error(f"test_update_post failed: {e}")
            pytest.fail(f"Update post failed: {e}")

    def test_delete_post(self, post_service):
        """
        Test to delete a post and verify the response.
        """
        post_service, logger, test_data = post_service
        post_id = test_data["delete_post"]["post_id"]
        try:
            response = post_service.delete_post(post_id)
            assert response == 200
            logger.info("test_delete_post passed.")
        except Exception as e:
            logger.error(f"test_delete_post failed: {e}")
            pytest.fail(f"Delete post failed: {e}")
