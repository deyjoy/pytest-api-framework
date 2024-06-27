def format_response(response):
    """
    Formats the API response into a dictionary containing the status code and JSON data.

    Args:
        response (requests.Response): The HTTP response object from the API request.

    Returns:
        dict: A dictionary with the status code and JSON data from the response.
    """
    return {
        "status_code": response.status_code,
        "json": response.json()
    }
