import json
import os
from src.schemas.response import HTTPResponses, HttpResponseModel
from src.service.meta.review_service_meta import ReviewServiceMeta

REVIEWS_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'db', 'db_avaliacoes.json')
USERS_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'db', 'db_usuarios.json')
RESERVAS_FILE_PATH = os.path.join(os.path.dirname(__file__), '..', '..', 'db', 'db_reservas.json')

def load_reviews():
    with open(REVIEWS_FILE_PATH, 'r') as file:
        return json.load(file)

def save_reviews(data):
    with open(REVIEWS_FILE_PATH, 'w') as file:
        json.dump(data, file, indent=4)

def load_users():
    with open(USERS_FILE_PATH, 'r') as file:
        return json.load(file)

def load_reservas():
    with open(RESERVAS_FILE_PATH, 'r') as file:
        return json.load(file)

class ReviewService(ReviewServiceMeta):

    @staticmethod
    def add_review(review_data: dict) -> HttpResponseModel:
        """Add a review method implementation"""
        reviews = load_reviews()
        review_data["id"] = len(reviews) + 1  # Adiciona um ID único à nova avaliação
        reviews.append(review_data)
        save_reviews(reviews)
        return HttpResponseModel(
            message=HTTPResponses.REVIEW_ADDED().message,
            status_code=HTTPResponses.REVIEW_ADDED().status_code,
            data=review_data,
        )

    @staticmethod
    def hide_review(cpfnj: str, comentario_id: int) -> HttpResponseModel:
        """Hide a review method implementation"""
        reviews = load_reviews()
        users = load_users()
        reservas = load_reservas()

        # Verificar se o usuário existe
        usuario = next((user for user in users if user["cpfnj"] == cpfnj), None)
        if not usuario:
            return HttpResponseModel(
                message=HTTPResponses.USER_NOT_FOUND().message,
                status_code=HTTPResponses.USER_NOT_FOUND().status_code,
            )

        # Encontrar a avaliação correspondente
        avaliacao = next((a for a in reviews if a["id"] == comentario_id), None)
        if not avaliacao:
            return HttpResponseModel(
                message=HTTPResponses.REVIEW_NOT_FOUND().message,
                status_code=HTTPResponses.REVIEW_NOT_FOUND().status_code,
            )

        # Encontrar a reserva correspondente ao endereço da avaliação
        reserva = next((r for r in reservas if r["endereco"] == avaliacao["endereco"]), None)
        if not reserva:
            return HttpResponseModel(
                message=HTTPResponses.RESERVATION_NOT_FOUND().message,
                status_code=HTTPResponses.RESERVATION_NOT_FOUND().status_code,
            )

        # Verificar se o CPF/CNPJ do usuário que quer ocultar corresponde ao CPF/CNPJ do dono da reserva
        if reserva["usuario"] != cpfnj:
            return HttpResponseModel(
                message=HTTPResponses.UNAUTHORIZED().message,
                status_code=HTTPResponses.UNAUTHORIZED().status_code,
            )

        # Marcar a avaliação como oculta
        avaliacao["oculto"] = True
        save_reviews(reviews)
        return HttpResponseModel(
            message=HTTPResponses.REVIEW_HIDDEN().message,
            status_code=HTTPResponses.REVIEW_HIDDEN().status_code,
        )

    @staticmethod
    def get_all_reviews():
        """Get all reviews method implementation"""
        reviews = load_reviews()
        return reviews