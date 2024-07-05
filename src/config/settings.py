import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API base URL from environment variables
API_BASE_URL = os.getenv('API_BASE_URL')

# Check if the API_BASE_URL environment variable is set
if not API_BASE_URL:
    raise ValueError("API_BASE_URL environment variable is not set. Please check your .env file.")

# Add additional environment variables as needed
# Example:
# API_TOKEN = os.getenv('API_TOKEN')
# if not API_TOKEN:
#     raise ValueError("API_TOKEN environment variable is not set. Please check your .env file.")
