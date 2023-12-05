from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from t08_flask_mysql.app.my_project.auth.controller import product_controller, available_snacks_controller
from t08_flask_mysql.app.my_project.auth.domain import Product
from t08_flask_mysql.app.my_project.auth.dao import available_snacks_dao

product_bp = Blueprint('product', __name__, url_prefix='/product')

@product_bp.get('/<int:product_id>/available_snacks')
def get_available_snacks_for_product(product_id: int) -> Response:
    """
    Gets all available snacks for a specific product.
    :param product_id: ID of the product
    :return: Response object
    """
    snacks = available_snacks_dao.find_by_product_id(product_id)
    snacks_dicts = [snack.put_into_dto() for snack in snacks]
    return make_response(jsonify(snacks_dicts), HTTPStatus.OK)

@product_bp.get('')
def get_all_products() -> Response:
    """
    Gets all products from the table.
    :return: Response object
    """
    return make_response(jsonify(product_controller.find_all()), HTTPStatus.OK)

@product_bp.post('')
def create_product() -> Response:
    """
    Creates a new product entry.
    :return: Response object
    """
    content = request.get_json()
    product = Product.create_from_dto(content)
    product_controller.create(product)
    return make_response(jsonify(product.put_into_dto()), HTTPStatus.CREATED)

@product_bp.get('/<int:product_id>')
def get_product(product_id: int) -> Response:
    """
    Gets a product by ID.
    :return: Response object
    """
    return make_response(jsonify(product_controller.find_by_id(product_id)), HTTPStatus.OK)

@product_bp.put('/<int:product_id>')
def update_product(product_id: int) -> Response:
    """
    Updates a product by ID.
    :return: Response object
    """
    content = request.get_json()
    product = Product.create_from_dto(content)
    product_controller.update(product_id, product)
    return make_response("Product updated", HTTPStatus.OK)

@product_bp.patch('/<int:product_id>')
def patch_product(product_id: int) -> Response:
    """
    Patches a product by ID.
    :return: Response object
    """
    content = request.get_json()
    product_controller.patch(product_id, content)
    return make_response("Product updated", HTTPStatus.OK)

@product_bp.delete('/<int:product_id>')
def delete_product(product_id: int) -> Response:
    """
    Deletes a product by ID.
    :return: Response object
    """
    product_controller.delete(product_id)
    return make_response("Product deleted", HTTPStatus.OK)
