from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.meta.review_service_meta import ReviewServiceMeta
from src.db.__init__ import database as db

class ReviewService(ReviewServiceMeta):

    @staticmethod
    def add_review(review_data: dict) -> HttpResponseModel:
        """Add a review method implementation"""
        review = db.add_review('reviews', review_data)
        if not review:
            return HttpResponseModel(
                message=HTTPResponses.REVIEW_NOT_ADDED().message,
                status_code=HTTPResponses.REVIEW_NOT_ADDED().status_code,
            )
        return HttpResponseModel(
            message=HTTPResponses.REVIEW_ADDED().message,
            status_code=HTTPResponses.REVIEW_ADDED().status_code,
            data=review,
        )

    @staticmethod
    def hide_review(cpfnj: str, comentario_id: int) -> HttpResponseModel:
        """Hide a review method implementation"""
        review = db.hide_review('reviews', cpfnj, comentario_id)
        if not review:
            return HttpResponseModel(
                message=HTTPResponses.REVIEW_NOT_FOUND().message,
                status_code=HTTPResponses.REVIEW_NOT_FOUND().status_code,
            )
        return HttpResponseModel(
            message=HTTPResponses.REVIEW_HIDDEN().message,
            status_code=HTTPResponses.REVIEW_HIDDEN().status_code,
        )

    @staticmethod
    def get_all_reviews():
        """Get all reviews method implementation"""
        return db.get_all_reviews()