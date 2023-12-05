from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import sold_snacks_controller
from t08_flask_mysql.app.my_project.auth.domain import SoldSnacks

sold_snacks_bp = Blueprint('sold_snacks', __name__, url_prefix='/sold_snacks')

@sold_snacks_bp.get('')
def get_all_sold_snacks() -> Response:
    """
    Gets all sold snacks from the table.
    :return: Response object
    """
    return make_response(jsonify(sold_snacks_controller.find_all()), HTTPStatus.OK)

@sold_snacks_bp.post('')
def create_sold_snack() -> Response:
    """
    Creates a new sold snack entry.
    :return: Response object
    """
    content = request.get_json()
    sold_snack = SoldSnacks.create_from_dto(content)
    sold_snacks_controller.create(sold_snack)
    return make_response(jsonify(sold_snack.put_into_dto()), HTTPStatus.CREATED)

@sold_snacks_bp.get('/<int:sold_snack_id>')
def get_sold_snack(sold_snack_id: int) -> Response:
    """
    Gets a sold snack by ID.
    :return: Response object
    """
    return make_response(jsonify(sold_snacks_controller.find_by_id(sold_snack_id)), HTTPStatus.OK)

@sold_snacks_bp.put('/<int:sold_snack_id>')
def update_sold_snack(sold_snack_id: int) -> Response:
    """
    Updates a sold snack by ID.
    :return: Response object
    """
    content = request.get_json()
    sold_snack = SoldSnacks.create_from_dto(content)
    sold_snacks_controller.update(sold_snack_id, sold_snack)
    return make_response("Sold snack updated", HTTPStatus.OK)

@sold_snacks_bp.patch('/<int:sold_snack_id>')
def patch_sold_snack(sold_snack_id: int) -> Response:
    """
    Patches a sold snack by ID.
    :return: Response object
    """
    content = request.get_json()
    sold_snacks_controller.patch(sold_snack_id, content)
    return make_response("Sold snack updated", HTTPStatus.OK)

@sold_snacks_bp.delete('/<int:sold_snack_id>')
def delete_sold_snack(sold_snack_id: int) -> Response:
    """
    Deletes a sold snack by ID.
    :return: Response object
    """
    sold_snacks_controller.delete(sold_snack_id)
    return make_response("Sold snack deleted", HTTPStatus.OK)
