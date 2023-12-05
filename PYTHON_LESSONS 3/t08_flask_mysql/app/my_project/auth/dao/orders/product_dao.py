from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Product


class ProductDAO(GeneralDAO):
    """
    Realisation of Product data access layer.
    """
    _domain_type = Product

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Product objects from the database table by field 'name'.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Product).filter(Product.name == name).order_by(Product.name).all()

    def find_by_brand(self, brand: str) -> List[object]:
        """
        Gets Product objects from the database table by field 'brand'.
        :param brand: brand value
        :return: search objects
        """
        return self._session.query(Product).filter(Product.brand == brand).order_by(Product.brand).all()

    def find_by_price_range(self, min_price: int, max_price: int) -> List[object]:
        """
        Gets Product objects from the database table within the specified price range.
        :param min_price: minimum price
        :param max_price: maximum price
        :return: search objects
        """
        return self._session.query(Product).filter(Product.price.between(min_price, max_price)).order_by(Product.price).all()

    def find_by_vending_machine_menu_id(self, vending_machine_menu_id: int):
        return self._session.query(Product).filter(Product.vending_machine_menu_id == vending_machine_menu_id).all()