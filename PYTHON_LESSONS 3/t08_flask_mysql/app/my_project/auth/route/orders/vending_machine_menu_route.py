from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import vending_machine_menu_controller
from t08_flask_mysql.app.my_project.auth.domain import VendingMachineMenu
from t08_flask_mysql.app.my_project.auth.dao import product_dao

vending_machine_menu_bp = Blueprint('vending_machine_menu', __name__, url_prefix='/vending_machine_menu')

@vending_machine_menu_bp.get('/<int:vending_machine_menu_id>/product')
def get_products_for_vending_machine_menu(vending_machine_menu_id: int) -> Response:
    """
    Gets all available snacks for a specific vending machine menu.
    :param vending_machine_menu_id: ID of the vending machine menu
    :return: Response object
    """
    products = product_dao.find_by_vending_machine_menu_id(vending_machine_menu_id)
    product_dicts = [product.put_into_dto() for product in products]
    return make_response(jsonify(product_dicts), HTTPStatus.OK)

@vending_machine_menu_bp.get('')
def get_all_vending_machine_menus() -> Response:
    """
    Gets all vending machine menus from the table.
    :return: Response object
    """
    return make_response(jsonify(vending_machine_menu_controller.find_all()), HTTPStatus.OK)

@vending_machine_menu_bp.post('')
def create_vending_machine_menu() -> Response:
    """
    Creates a new vending machine menu entry.
    :return: Response object
    """
    content = request.get_json()
    vending_machine_menu = VendingMachineMenu.create_from_dto(content)
    vending_machine_menu_controller.create(vending_machine_menu)
    return make_response(jsonify(vending_machine_menu.put_into_dto()), HTTPStatus.CREATED)

@vending_machine_menu_bp.get('/<int:vending_machine_menu_id>')
def get_vending_machine_menu(vending_machine_menu_id: int) -> Response:
    """
    Gets a vending machine menu by ID.
    :return: Response object
    """
    return make_response(jsonify(vending_machine_menu_controller.find_by_id(vending_machine_menu_id)), HTTPStatus.OK)

@vending_machine_menu_bp.put('/<int:vending_machine_menu_id>')
def update_vending_machine_menu(vending_machine_menu_id: int) -> Response:
    """
    Updates a vending machine menu by ID.
    :return: Response object
    """
    content = request.get_json()
    vending_machine_menu = VendingMachineMenu.create_from_dto(content)
    vending_machine_menu_controller.update(vending_machine_menu_id, vending_machine_menu)
    return make_response("Vending machine menu updated", HTTPStatus.OK)

@vending_machine_menu_bp.patch('/<int:vending_machine_menu_id>')
def patch_vending_machine_menu(vending_machine_menu_id: int) -> Response:
    """
    Patches a vending machine menu by ID.
    :return: Response object
    """
    content = request.get_json()
    vending_machine_menu_controller.patch(vending_machine_menu_id, content)
    return make_response("Vending machine menu updated", HTTPStatus.OK)

@vending_machine_menu_bp.delete('/<int:vending_machine_menu_id>')
def delete_vending_machine_menu(vending_machine_menu_id: int) -> Response:
    """
    Deletes a vending machine menu by ID.
    :return: Response object
    """
    vending_machine_menu_controller.delete(vending_machine_menu_id)
    return make_response("Vending machine menu deleted", HTTPStatus.OK)
