import requests
from requests.exceptions import HTTPError, RequestException
from src.config.settings import API_BASE_URL


class APIClient:
    """
    APIClient is a class that provides methods to interact with a RESTful API.
    It supports GET, POST, PUT, and DELETE requests.

    Attributes:
        base_url (str): The base URL for the API.
    """

    def __init__(self, base_url=API_BASE_URL):
        """
        Initializes the APIClient with the given base URL.

        Args:
            base_url (str): The base URL for the API. Defaults to API_BASE_URL from settings.
        """
        self.base_url = base_url

    def _request(self, method, endpoint, **kwargs):
        """
        Internal method to handle HTTP requests.

        Args:
            method (str): The HTTP method (e.g., 'GET', 'POST', etc.).
            endpoint (str): The API endpoint.
            **kwargs: Additional keyword arguments to pass to the request.

        Returns:
            dict or int: The JSON response for 'GET', 'POST', and 'PUT' requests, or the status code for 'DELETE'.

        Raises:
            HTTPError: An error occurred during the HTTP request.
            RequestException: A non-HTTP error occurred (e.g., network issues).
        """
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.request(method, url, **kwargs)
            response.raise_for_status()
            if method == 'DELETE':
                return response.status_code
            return response.json()
        except HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            raise
        except RequestException as req_err:
            print(f"Request error occurred: {req_err}")
            raise

    def get(self, endpoint):
        """
        Sends a GET request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint.

        Returns:
            dict: The JSON response.
        """
        return self._request('GET', endpoint)

    def post(self, endpoint, data):
        """
        Sends a POST request to the specified endpoint with the given data.

        Args:
            endpoint (str): The API endpoint.
            data (dict): The JSON payload to send in the request body.

        Returns:
            dict: The JSON response.
        """
        return self._request('POST', endpoint, json=data)

    def put(self, endpoint, data):
        """
        Sends a PUT request to the specified endpoint with the given data.

        Args:
            endpoint (str): The API endpoint.
            data (dict): The JSON payload to send in the request body.

        Returns:
            dict: The JSON response.
        """
        return self._request('PUT', endpoint, json=data)

    def delete(self, endpoint):
        """
        Sends a DELETE request to the specified endpoint.

        Args:
            endpoint (str): The API endpoint.

        Returns:
            int: The status code of the response.
        """
        return self._request('DELETE', endpoint)
