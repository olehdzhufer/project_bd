from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import collection_controller
from t08_flask_mysql.app.my_project.auth.domain import Collection

collection_bp = Blueprint('collection', __name__, url_prefix='/collection')

@collection_bp.get('')
def get_all_collection() -> Response:
    """
    Gets all sold snacks from the table.
    :return: Response object
    """
    return make_response(jsonify(collection_controller.find_all()), HTTPStatus.OK)

@collection_bp.post('')
def create_collection() -> Response:
    """
    Creates a new sold snack entry.
    :return: Response object
    """
    content = request.get_json()
    collection = Collection.create_from_dto(content)
    collection_controller.create(collection)
    return make_response(jsonify(collection.put_into_dto()), HTTPStatus.CREATED)

@collection_bp.get('/<int:collection_id>')
def get_collection(collection_id: int) -> Response:
    """
    Gets a sold snack by ID.
    :return: Response object
    """
    return make_response(jsonify(collection_controller.find_by_id(collection_id)), HTTPStatus.OK)

@collection_bp.put('/<int:collection_id>')
def update_collection(collection_id: int) -> Response:
    """
    Updates a sold snack by ID.
    :return: Response object
    """
    content = request.get_json()
    collection = Collection.create_from_dto(content)
    collection_controller.update(collection_id, collection)
    return make_response("Collection updated", HTTPStatus.OK)

@collection_bp.patch('/<int:collection_id>')
def patch_collection(collection_id: int) -> Response:
    """
    Patches a sold snack by ID.
    :return: Response object
    """
    content = request.get_json()
    collection_controller.patch(collection_id, content)
    return make_response("Collection updated", HTTPStatus.OK)

@collection_bp.delete('/<int:collection_id>')
def delete_collection(collection_id: int) -> Response:
    """
    Deletes a sold snack by ID.
    :return: Response object
    """
    collection_controller.delete(collection_id)
    return make_response("Collection deleted", HTTPStatus.OK)
