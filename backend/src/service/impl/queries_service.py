from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.meta.query_service_meta import QueryServiceMeta
from src.db.__init__ import database as db

class QueriesService(QueryServiceMeta):

    @staticmethod
    def get_queries(filters: dict) -> HttpResponseModel:
        """Get queries based on filters method implementation"""
        queries = db.get_filtered_queries('reservas', filters)
        if not queries:
            return HttpResponseModel(
                message=HTTPResponses.QUERIES_NOT_FOUND().message,
                status_code=HTTPResponses.QUERIES_NOT_FOUND().status_code,
            )

        return HttpResponseModel(
            message=HTTPResponses.QUERIES_FOUND().message,
            status_code=HTTPResponses.QUERIES_FOUND().status_code,
            data=queries,
        )