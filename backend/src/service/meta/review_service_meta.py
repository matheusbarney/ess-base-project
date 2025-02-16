from abc import ABC, abstractmethod
from src.schemas.response import HttpResponseModel

class ReviewServiceMeta(ABC):

    @abstractmethod
    def add_review(self, review_data: dict) -> HttpResponseModel:
        """Add a review method definition"""
        pass

    @abstractmethod
    def hide_review(self, cpfnj: str, comentario_id: int) -> HttpResponseModel:
        """Hide a review method definition"""
        pass