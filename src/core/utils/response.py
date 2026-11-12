from src.core.schemas.common import ApiResponse


def success_response[T](message: str, data: T | None = None) -> ApiResponse[T]:
    """
    Generate a success response.

    Args:
        message (str): The success message.
        data (T | None): The optional data to include in the response.

    Returns:
        ApiResponse[T]: A success response object.
    """
    return ApiResponse(status=True, message=message, data=data)


def error_response[T](message: str, data: T | None = None) -> ApiResponse[T]:
    """
    Generate an error response.

    Args:
        message (str): The error message.
        data (T | None): The optional data to include in the response.

    Returns:
        ApiResponse[T]: An error response object.
    """
    return ApiResponse(status=False, message=message, data=data)