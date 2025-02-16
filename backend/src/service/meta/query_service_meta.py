from abc import ABC, abstractmethod
from src.schemas.response import HttpResponseModel

class QueryServiceMeta(ABC):

    @abstractmethod
    def get_queries(self, filters: dict) -> HttpResponseModel:
        """Get queries based on filters method definition"""
        pass