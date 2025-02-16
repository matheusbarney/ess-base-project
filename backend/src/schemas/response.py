from typing import Optional
from pydantic import BaseModel

class HttpResponseModel(BaseModel):
    message: str
    status_code: int
    data: Optional[dict] | Optional[list] = None

class HTTPResponses:

    """
    This class contains the basic HTTP responses for the API
    """

    @staticmethod
    def ITEM_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Item not found",
            status_code=404,
        )

    @staticmethod
    def ITEM_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Item found",
            status_code=200,
        )

    @staticmethod
    def ITEM_CREATED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Item created",
            status_code=201,
        )

    @staticmethod
    def SERVER_ERROR() -> HttpResponseModel:
        return HttpResponseModel(
            message="Server error",
            status_code=500,
        )

    @staticmethod
    def REVIEW_ADDED() -> HttpResponseModel:
        return HttpResponseModel(
            message="Review added successfully",
            status_code=200,
        )

    @staticmethod
    def REVIEW_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Review not found",
            status_code=404,
        )

    @staticmethod
    def REVIEW_HIDDEN() -> HttpResponseModel:
        return HttpResponseModel(
            message="Review hidden successfully",
            status_code=200,
        )

    @staticmethod
    def QUERIES_NOT_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="No reservations found with the given filters",
            status_code=404,
        )

    @staticmethod
    def QUERIES_FOUND() -> HttpResponseModel:
        return HttpResponseModel(
            message="Reservations found",
            status_code=200,
        )