import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Example configuration variables
# API_BASE_URL: The base URL for the API. Default is 'https://jsonplaceholder.typicode.com' if not set in the .env file.
API_BASE_URL = os.getenv('API_BASE_URL', 'https://jsonplaceholder.typicode.com')
