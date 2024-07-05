import pytest
from src.services.comment_service import CommentService
from src.config.logging_config import configure_logging, get_logger
from datetime import datetime

# Configure logging with a unique log file for this test run
log_file = f'logs/test_comments_{datetime.now().strftime("%Y%m%d_%H%M%S")}.log'
configure_logging(log_file)
logger = get_logger(__name__)


class TestCommentsAPI:
    """
    Test class for Comments API.
    Encapsulates test cases for the Comments endpoints.
    """

    @classmethod
    def setup_class(cls):
        """
        Setup for the entire test class.
        Initializes the CommentService.
        """
        cls.comment_service = CommentService()
        logger.info("Initialized CommentService for test class.")

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

    def test_get_comments(self):
        """
        Test to get all comments and verify the response.
        """
        try:
            response = self.comment_service.fetch_all_comments()
            assert len(response) > 0
            logger.info("test_get_comments passed.")
        except Exception as e:
            logger.error(f"test_get_comments failed: {e}")
            pytest.fail(f"Get comments failed: {e}")

    def test_get_comment_by_id(self):
        """
        Test to get a comment by ID and verify the response.
        """
        comment_id = 1
        try:
            response = self.comment_service.fetch_comment_by_id(comment_id)
            assert response['id'] == comment_id
            logger.info("test_get_comment_by_id passed.")
        except Exception as e:
            logger.error(f"test_get_comment_by_id failed: {e}")
            pytest.fail(f"Get comment by ID failed: {e}")

    def test_create_comment(self):
        """
        Test to create a new comment and verify the response.
        """
        new_comment = {
            'name': 'foo',
            'body': 'bar',
            'postId': 1,
            'email': 'foo@bar.com'
        }
        try:
            response = self.comment_service.create_comment(new_comment)
            assert response['name'] == new_comment['name']
            logger.info("test_create_comment passed.")
        except Exception as e:
            logger.error(f"test_create_comment failed: {e}")
            pytest.fail(f"Create comment failed: {e}")

    def test_update_comment(self):
        """
        Test to update a comment and verify the response.
        """
        comment_id = 1
        updated_comment = {
            'id': comment_id,
            'name': 'updated name',
            'body': 'updated body',
            'postId': 1,
            'email': 'updated@bar.com'
        }
        try:
            response = self.comment_service.update_comment(comment_id, updated_comment)
            assert response['name'] == updated_comment['name']
            logger.info("test_update_comment passed.")
        except Exception as e:
            logger.error(f"test_update_comment failed: {e}")
            pytest.fail(f"Update comment failed: {e}")

    def test_delete_comment(self):
        """
        Test to delete a comment and verify the response.
        """
        comment_id = 1
        try:
            response = self.comment_service.delete_comment(comment_id)
            assert response == 200
            logger.info("test_delete_comment passed.")
        except Exception as e:
            logger.error(f"test_delete_comment failed: {e}")
            pytest.fail(f"Delete comment failed: {e}")
