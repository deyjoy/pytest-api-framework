import logging
import os
from datetime import datetime
from functools import wraps


def configure_logging(log_file=None):
    """Configure logging for the application."""
    if log_file is None:
        # Generate a unique log file name based on the current timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        log_file = f'logs/app_{timestamp}.log'

    # Ensure the directory for log files exists
    log_dir = os.path.dirname(log_file)
    if log_dir and not os.path.exists(log_dir):
        os.makedirs(log_dir)

    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Clear existing handlers
    if logger.hasHandlers():
        logger.handlers.clear()

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(console_formatter)

    # File handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(logging.INFO)
    file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(file_formatter)

    # Add handlers to the logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    logger.info("Logging configuration completed successfully.")


def get_logger(name):
    """Get a logger with the given name."""
    return logging.getLogger(name)


def log_with_file(file_name):
    """Decorator to configure logging for the duration of a method call."""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            configure_logging(file_name)
            logger = get_logger(__name__)
            logger.info(f"Starting method {func.__name__}")
            try:
                result = func(*args, **kwargs)
                logger.info(f"Finished method {func.__name__}")
                return result
            except Exception as e:
                logger.error(f"An error occurred in method {func.__name__}: {e}")
                raise

        return wrapper

    return decorator
