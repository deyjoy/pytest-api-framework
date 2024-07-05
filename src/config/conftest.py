import pytest
from src.utils.logging_utils import setup_logging


@pytest.fixture(scope='session', autouse=True)
def configure_logging_session():
    """
    Session-wide logging configuration.
    """
    logger = setup_logging('session')
    yield logger
    # Perform any cleanup if necessary after the session
