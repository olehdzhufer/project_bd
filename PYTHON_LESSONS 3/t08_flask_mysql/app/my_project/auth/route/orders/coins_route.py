from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import coins_controller
from t08_flask_mysql.app.my_project.auth.domain import Coins

coins_bp = Blueprint('coins', __name__, url_prefix='/coins')

@coins_bp.get('')
def get_all_coins() -> Response:
    """
    Gets all sold snacks from the table.
    :return: Response object
    """
    return make_response(jsonify(coins_controller.find_all()), HTTPStatus.OK)

@coins_bp.post('')
def create_coins() -> Response:
    """
    Creates a new sold snack entry.
    :return: Response object
    """
    content = request.get_json()
    coins = Coins.create_from_dto(content)
    coins_controller.create(coins)
    return make_response(jsonify(coins.put_into_dto()), HTTPStatus.CREATED)

@coins_bp.get('/<int:coins_id>')
def get_coins(coins_id: int) -> Response:
    """
    Gets a sold snack by ID.
    :return: Response object
    """
    return make_response(jsonify(coins_controller.find_by_id(coins_id)), HTTPStatus.OK)

@coins_bp.put('/<int:coins_id>')
def update_coins(coins_id: int) -> Response:
    """
    Updates a sold snack by ID.
    :return: Response object
    """
    content = request.get_json()
    coins = Coins.create_from_dto(content)
    coins_controller.update(coins_id, coins)
    return make_response("Coins updated", HTTPStatus.OK)

@coins_bp.patch('/<int:coins_id>')
def patch_coins(coins_id: int) -> Response:
    """
    Patches a sold snack by ID.
    :return: Response object
    """
    content = request.get_json()
    coins_controller.patch(coins_id, content)
    return make_response("Coins updated", HTTPStatus.OK)

@coins_bp.delete('/<int:coins_id>')
def delete_coins(coins_id: int) -> Response:
    """
    Deletes a sold snack by ID.
    :return: Response object
    """
    coins_controller.delete(coins_id)
    return make_response("Coins deleted", HTTPStatus.OK)
