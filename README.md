# API Testing with Pytest

This project demonstrates API testing using Pytest in Python. The tests are written to validate the endpoints of the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/).

## Folder Structure

The project follows a structured design pattern to ensure maintainability and reusability. The key components include:

- **api/**: Contains the API client code to interact with the JSONPlaceholder API.
- **config/**: Configuration files for environment settings and logging.
- **services/**: Service classes encapsulating the business logic and interactions with the API endpoints.
- **tests/**: Test cases organized by API endpoints.
- **utils/**: Utility functions and helper methods.
- **data/**: JSON files for test data.
- **.github/**: GitHub Actions workflows for CI/CD.

```plaintext
project_root/
│
├── src/
│   ├── __init__.py
│   ├── api/
│   │   ├── __init__.py
│   │   ├── clients.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── logging_config.py
│   │   ├── settings.py
│   │   ├── conftest.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── post_service.py
│   │   ├── comment_service.py
│   │   ├── user_service.py
│   │   ├── album_service.py
│   │   ├── photo_service.py
│   │   ├── todo_service.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_posts.py
│   │   ├── test_comments.py
│   │   ├── test_users.py
│   │   ├── test_albums.py
│   │   ├── test_photos.py
│   │   ├── test_todos.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py
│   │   ├── logging_utils.py
│   ├── data/
│   │   ├── albums_test_data.json
│   │   ├── comments_test_data.json
│   │   ├── photos_test_data.json
│   │   ├── posts_test_data.json
│   │   ├── todos_test_data.json
│   │   ├── users_test_data.json
│
├── .github/
│   ├── workflows/
│   │   ├── ci.yml
│
├── .env
├── .gitignore
├── README.md
├── requirements.txt
└── pytest.ini
```

## Design Patterns

### Service Layer Pattern: 
Each service class in the services/ directory encapsulates the business logic and interactions with the API endpoints, promoting modularity and reusability.


### Utility Functions: 
Common helper methods are placed in the utils/ directory to keep the codebase DRY (Don't Repeat Yourself).

## Setup Instructions

### Clone the Repository:
```commandline
git clone <repository-url>
cd project_root
```

### Set Up Virtual Environment:
```commandline
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install Dependencies:
```commandline
pip install -r requirements.txt

```

### Configure Environment Variables
Create a .env file in the root directory and add any necessary environment variables.

### Logging Configuration
Logging configuration is centralized in src/config/logging_config.py. The configure_logging function sets up logging with a unique log file for each test run.

### Logging Utility
The logging utility in src/utils/logging_utils.py provides a setup_logging function to configure logging for test runs based on the test name.

### Test Data Management
Test data is stored in JSON files under the src/data directory. Each test file loads the necessary test data using pytest fixtures.

### Test Files
Each test file initializes the necessary service and loads test data through fixtures. Logging is set up using the setup_logging function from the logging utility.

### Run the Setup Script:
If you haven't already set up the folder structure, you can run the provided script:
```commandline
python setup_structure.py

```

### Running Tests
```commandline
pytest
```

### CI Integration
This project uses GitHub Actions for Continuous Integration. The configuration file is located at .github/workflows/ci.yml.
You can replace `<repository-url>` with the actual URL of your repository.





