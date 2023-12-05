from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import vending_machine_controller
from t08_flask_mysql.app.my_project.auth.domain import VendingMachine
from t08_flask_mysql.app.my_project.auth.domain.orders.coins import Coins
from t08_flask_mysql.app.my_project.auth.domain.orders.coins_and_vending_machines import CoinsAndVendingMachine
from t08_flask_mysql.app.my_project.auth.domain.orders.collection import Collection
from t08_flask_mysql.app.my_project.auth.domain.orders.collection_and_vending_machines import \
    CollectionAndVendingMachine
from t08_flask_mysql.app.my_project.auth.domain.orders.sold_snack_and_vending_machine import SoldSnackAndVendingMachine
from t08_flask_mysql.app.my_project.auth.domain.orders.sold_snacks import SoldSnacks
from t08_flask_mysql.app.my_project.auth.domain.orders.technican import Technican
from t08_flask_mysql.app.my_project.auth.domain.orders.technican_and_vending_machines import TechnicanAndVendingMachine

vending_machine_bp = Blueprint('vending_machine', __name__, url_prefix='/vending_machine')

@vending_machine_bp.get('collection')
def get_all_collection_for_vending_machine_data() -> Response:
    array = []
    collections = Collection.query.all()
    for collection in collections:
        for vending in collection.vending_machines:
            vending_machine = vending.vending_machine
            array.append(CollectionAndVendingMachine(collection.collection_date, collection.collected__amount, vending_machine.address, vending_machine.gps_coordinates, vending_machine.last_loading_date).to_dict())
    return make_response(jsonify(array), HTTPStatus.OK)



@vending_machine_bp.get('coins')
def get_all_coins_for_vending_machine_data() -> Response:
    array = []
    coins = Coins.query.all()
    for coin in coins:
        for vending in coin.vending_machines:
            vending_machine = vending.vending_machine
            array.append(CoinsAndVendingMachine(coin.coin_loading_date, coin.coin_amount, vending_machine.address, vending_machine.gps_coordinates, vending_machine.last_loading_date).to_dict())
    return make_response(jsonify(array), HTTPStatus.OK)


@vending_machine_bp.get('technicans')
def get_all_technican_for_vending_machine_data() -> Response:
    array = []
    technicans = Technican.query.all()
    for technician in technicans:
        for vending in technician.vending_machines:
            vending_machine = vending.vending_machine
            array.append(TechnicanAndVendingMachine(technician.name, vending_machine.address, vending_machine.gps_coordinates, vending_machine.last_loading_date).to_dict())
    return make_response(jsonify(array), HTTPStatus.OK)


@vending_machine_bp.get('sold_snacks')
def get_all_sold_snack_for_vending_machine_data() -> Response:
    array = []
    snacks = SoldSnacks.query.all()
    for snack in snacks:
        for vending in snack.vending_machines:
            vending_machine = vending.vending_machine
            array.append(SoldSnackAndVendingMachine(snack.sale_data, snack.quantity_sold, vending_machine.address, vending_machine.gps_coordinates, vending_machine.last_loading_date).to_dict())
    return make_response(jsonify(array), HTTPStatus.OK)

@vending_machine_bp.get('')
def get_all_vending_machines() -> Response:
    """
    Gets all vending machines from the table.
    :return: Response object
    """
    return make_response(jsonify(vending_machine_controller.find_all()), HTTPStatus.OK)

@vending_machine_bp.post('')
def create_vending_machine() -> Response:
    """
    Creates a new vending machine entry.
    :return: Response object
    """
    content = request.get_json()
    vending_machine = VendingMachine.create_from_dto(content)
    vending_machine_controller.create(vending_machine)
    return make_response(jsonify(vending_machine.put_into_dto()), HTTPStatus.CREATED)

@vending_machine_bp.get('/<int:vending_machine_id>')
def get_vending_machine(vending_machine_id: int) -> Response:
    """
    Gets a vending machine by ID.
    :return: Response object
    """
    return make_response(jsonify(vending_machine_controller.find_by_id(vending_machine_id)), HTTPStatus.OK)

@vending_machine_bp.put('/<int:vending_machine_id>')
def update_vending_machine(vending_machine_id: int) -> Response:
    """
    Updates a vending machine by ID.
    :return: Response object
    """
    content = request.get_json()
    vending_machine = VendingMachine.create_from_dto(content)
    vending_machine_controller.update(vending_machine_id, vending_machine)
    return make_response("Vending machine updated", HTTPStatus.OK)

@vending_machine_bp.patch('/<int:vending_machine_id>')
def patch_vending_machine(vending_machine_id: int) -> Response:
    """
    Patches a vending machine by ID.
    :return: Response object
    """
    content = request.get_json()
    vending_machine_controller.patch(vending_machine_id, content)
    return make_response("Vending machine updated", HTTPStatus.OK)

@vending_machine_bp.delete('/<int:vending_machine_id>')
def delete_vending_machine(vending_machine_id: int) -> Response:
    """
    Deletes a vending machine by ID.
    :return: Response object
    """
    vending_machine_controller.delete(vending_machine_id)
    return make_response("Vending machine deleted", HTTPStatus.OK)
