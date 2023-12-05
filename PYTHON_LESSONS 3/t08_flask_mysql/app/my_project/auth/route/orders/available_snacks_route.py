from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response

from t08_flask_mysql.app.my_project.auth.controller import available_snacks_controller
from t08_flask_mysql.app.my_project.auth.domain import AvailableSnacks


available_snacks_bp = Blueprint('available_snacks', __name__, url_prefix='/available_snacks')



@available_snacks_bp.get('')
def get_all_available_snacks() -> Response:
    return make_response(jsonify(available_snacks_controller.find_all()), HTTPStatus.OK)


@available_snacks_bp.post('')
def create_available_snacks() -> Response:
    """
    Creates a new sold snack entry.
    :return: Response object
    """
    content = request.get_json()
    available_snacks = AvailableSnacks.create_from_dto(content)
    available_snacks_controller.create(available_snacks)
    return make_response(jsonify(available_snacks.put_into_dto()), HTTPStatus.CREATED)


@available_snacks_bp.get('/<int:available_snscks_id>')
def get_available_snacks(available_snacks_id: int) -> Response:
    """
    Gets a sold snack by ID.
    :return: Response object
    """
    return make_response(jsonify(available_snacks_controller.find_by_id(available_snacks_id)), HTTPStatus.OK)


@available_snacks_bp.put('/<int:available_snacks_id>')
def update_available_snacks(available_snacks_id: int) -> Response:
    """
    Updates a sold snack by ID.
    :return: Response object
    """
    content = request.get_json()
    available_snacks = AvailableSnacks.create_from_dto(content)
    available_snacks_controller.update(available_snacks_id, available_snacks)
    return make_response("Available snacks updated", HTTPStatus.OK)


@available_snacks_bp.patch('/<int:available_snacks_id>')
def patch_available_snacks(available_snacks_id: int) -> Response:
    """
    Patches a sold snack by ID.
    :return: Response object
    """
    content = request.get_json()
    available_snacks_controller.patch(available_snacks_id, content)
    return make_response("Available snacks updated", HTTPStatus.OK)


@available_snacks_bp.delete('/<int:available_snacks_id>')
def delete_available_snacks(available_snacks_id: int) -> Response:
    """
    Deletes a sold snack by ID.
    :return: Response object
    """
    available_snacks_controller.delete(available_snacks_id)
    return make_response("Available snacks deleted", HTTPStatus.OK)
