import pytest
import json
import os
from src.services.comment_service import CommentService
from src.utils.logging_utils import setup_logging


@pytest.fixture(scope='class')
def comment_service():
    service = CommentService()
    logger = setup_logging('comments')
    logger.info("Initialized CommentService for test class.")
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(base_dir, '../data/comments_test_data.json')
    with open(data_file) as f:
        test_data = json.load(f)
    return service, logger, test_data


class TestCommentsAPI:
    """
    Test class for Comments API.
    Encapsulates test cases for the Comments endpoints.
    """

    def test_get_comments(self, comment_service):
        """
        Test to get all comments and verify the response.
        """
        comment_service, logger, test_data = comment_service
        try:
            response = comment_service.fetch_all_comments()
            assert len(response) > 0
            logger.info("test_get_comments passed.")
        except Exception as e:
            logger.error(f"test_get_comments failed: {e}")
            pytest.fail(f"Get comments failed: {e}")

    def test_get_comment_by_id(self, comment_service):
        """
        Test to get a comment by ID and verify the response.
        """
        comment_service, logger, test_data = comment_service
        comment_id = test_data["get_comment_by_id"]["comment_id"]
        try:
            response = comment_service.fetch_comment_by_id(comment_id)
            assert response['id'] == comment_id
            logger.info("test_get_comment_by_id passed.")
        except Exception as e:
            logger.error(f"test_get_comment_by_id failed: {e}")
            pytest.fail(f"Get comment by ID failed: {e}")

    def test_create_comment(self, comment_service):
        """
        Test to create a new comment and verify the response.
        """
        comment_service, logger, test_data = comment_service
        new_comment = test_data["create_comment"]["new_comment"]
        try:
            response = comment_service.create_comment(new_comment)
            assert response['name'] == new_comment['name']
            logger.info("test_create_comment passed.")
        except Exception as e:
            logger.error(f"test_create_comment failed: {e}")
            pytest.fail(f"Create comment failed: {e}")

    def test_update_comment(self, comment_service):
        """
        Test to update a comment and verify the response.
        """
        comment_service, logger, test_data = comment_service
        comment_id = test_data["update_comment"]["comment_id"]
        updated_comment = test_data["update_comment"]["updated_comment"]
        try:
            response = comment_service.update_comment(comment_id, updated_comment)
            assert response['name'] == updated_comment['name']
            logger.info("test_update_comment passed.")
        except Exception as e:
            logger.error(f"test_update_comment failed: {e}")
            pytest.fail(f"Update comment failed: {e}")

    def test_delete_comment(self, comment_service):
        """
        Test to delete a comment and verify the response.
        """
        comment_service, logger, test_data = comment_service
        comment_id = test_data["delete_comment"]["comment_id"]
        try:
            response = comment_service.delete_comment(comment_id)
            assert response == 200
            logger.info("test_delete_comment passed.")
        except Exception as e:
            logger.error(f"test_delete_comment failed: {e}")
            pytest.fail(f"Delete comment failed: {e}")
