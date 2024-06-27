from src.api.clients import APIClient


class TestPostsAPI:
    @classmethod
    def setup_class(cls):
        """Setup for the entire class. Runs once before all tests."""
        cls.client = APIClient()

    def test_get_posts(self):
        """Test to get all posts and verify the response."""
        response = self.client.get('posts')
        assert response is not None
