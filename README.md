# API Testing with Pytest

This project demonstrates API testing using Pytest in Python. The tests are written to validate the endpoints of the [JSONPlaceholder API](https://jsonplaceholder.typicode.com/).

## Folder Structure

The project follows a structured design pattern to ensure maintainability and reusability. The key components include:

- **api/**: Contains the API client code to interact with the JSONPlaceholder API.
- **config/**: Configuration files for environment settings.
- **data/**: Test data files for data-driven testing.
- **services/**: Service classes encapsulating the business logic and interactions with the API endpoints.
- **tests/**: Test cases organized by API endpoints.
- **utils/**: Utility functions and helper methods.

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
│   │   ├── settings.py
│   ├── data/
│   │   ├── test_data.json
│   ├── services/
│   │   ├── __init__.py
│   │   ├── post_service.py
│   │   ├── comment_service.py
│   │   ├── user_service.py
│   │   ├── album_service.py
│   │   ├── photo_service.py
│   │   ├── todo_service.py
│   │   ├── api_factory.py
│   ├── tests/
│   │   ├── __init__.py
│   │   ├── test_endpoints.py
│   │   ├── test_posts.py
│   │   ├── test_comments.py
│   │   ├── test_users.py
│   │   ├── test_albums.py
│   │   ├── test_photos.py
│   │   ├── test_todos.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py
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

### Data-Driven Testing: 
Test data is managed in the data/ directory, allowing for flexible and scalable test cases.

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
### Run the Setup Script:
If you haven't already set up the folder structure, you can run the provided script:
```commandline
python setup_structure.py

```
### Configure Environment Variables:
Create a .env file in the root directory and add any necessary environment variables.

### Running Tests
```commandline
pytest
```

### CI Integration
This project uses GitHub Actions for Continuous Integration. The configuration file is located at .github/workflows/ci.yml.
You can replace `<repository-url>` with the actual URL of your repository.





