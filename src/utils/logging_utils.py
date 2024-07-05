from src.config.logging_config import configure_logging, get_logger


def setup_logging(test_name: str):
    """
    Configures logging for a test run with a unique log file based on the test name.
    """
    log_file = f'logs/test_{test_name}.log'
    configure_logging(log_file)
    return get_logger(test_name)
