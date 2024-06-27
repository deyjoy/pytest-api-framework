from src.api.clients import APIClient
from src.utils.logging_config import get_logger, log_with_file, configure_logging

logger = get_logger(__name__)


class TestPostsAPI:
    @classmethod
    def setup_class(cls):
        """Setup for the entire class. Runs once before all tests."""
        log_file = f"logs/{cls.__name__}.log"
        configure_logging(log_file)
        logger.info("Setting up TestPostsAPI class...")
        cls.client = APIClient()

    @log_with_file("logs/TestPostsAPI_test_get_posts.log")
    def test_get_posts(self):
        """Test to get all posts and verify the response."""
        logger.info("Starting test: test_get_posts")
        try:
            response = self.client.get('posts')
            logger.info(f"Response received: {response}")

            assert response is not None
            logger.info("Test test_get_posts passed.")
        except Exception as e:
            logger.error(f"An error occurred in test_get_posts: {e}")
            raise
