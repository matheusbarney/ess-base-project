import json
import os
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.meta.query_service_meta import QueryServiceMeta

DATA_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'db', 'db_reservas.json')

def load_data():
    with open(DATA_FILE_PATH, 'r') as file:
        return json.load(file)

def save_data(data):
    with open(DATA_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

class QueriesService(QueryServiceMeta):

    @staticmethod
    def get_queries(filters: dict) -> HttpResponseModel:
        """Get queries based on filters method implementation"""
        data = load_data()
        queries = [item for item in data if all(
            item.get(key) == value for key, value in filters.items()
        )]
        
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