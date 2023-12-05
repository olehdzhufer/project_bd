from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import technican_controller
from t08_flask_mysql.app.my_project.auth.domain import Technican

technican_bp = Blueprint('technican', __name__, url_prefix='/technican')

@technican_bp.get('')
def get_all_technicans() -> Response:
    """
    Gets all technicans from the table.
    :return: Response object
    """
    return make_response(jsonify(technican_controller.find_all()), HTTPStatus.OK)

@technican_bp.post('')
def create_technican() -> Response:
    """
    Creates a new technican entry.
    :return: Response object
    """
    content = request.get_json()
    technican = Technican.create_from_dto(content)
    technican_controller.create(technican)
    return make_response(jsonify(technican.put_into_dto()), HTTPStatus.CREATED)

@technican_bp.get('/<int:technican_id>')
def get_technican(technican_id: int) -> Response:
    """
    Gets a technican by ID.
    :return: Response object
    """
    return make_response(jsonify(technican_controller.find_by_id(technican_id)), HTTPStatus.OK)

@technican_bp.put('/<int:technican_id>')
def update_technican(technican_id: int) -> Response:
    """
    Updates a technican by ID.
    :return: Response object
    """
    content = request.get_json()
    technican = Technican.create_from_dto(content)
    technican_controller.update(technican_id, technican)
    return make_response("Technican updated", HTTPStatus.OK)

@technican_bp.patch('/<int:technican_id>')
def patch_technican(technican_id: int) -> Response:
    """
    Patches a technican by ID.
    :return: Response object
    """
    content = request.get_json()
    technican_controller.patch(technican_id, content)
    return make_response("Technican updated", HTTPStatus.OK)

@technican_bp.delete('/<int:technican_id>')
def delete_technican(technican_id: int) -> Response:
    """
    Deletes a technican by ID.
    :return: Response object
    """
    technican_controller.delete(technican_id)
    return make_response("Technican deleted", HTTPStatus.OK)
