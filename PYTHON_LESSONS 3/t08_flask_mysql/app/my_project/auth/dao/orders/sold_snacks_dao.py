from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import SoldSnacks


class SoldSnacksDAO(GeneralDAO):
    """
    Realisation of Sold Snacks data access layer.
    """
    _domain_type = SoldSnacks

    def find_by_sale_data(self, sale_data: str) -> List[object]:
        """
        Gets Sold Snacks objects from the database table by field 'sale_data'.
        :param sale_data: sale_data value
        :return: search objects
        """
        return self._session.query(SoldSnacks).filter(SoldSnacks.sale_data == sale_data).order_by(SoldSnacks.sale_data).all()

    def find_by_quantity_sold(self, quantity_sold: int) -> List[object]:
        """
        Gets Sold Snacks objects from the database table by field 'quantity_sold'.
        :param quantity_sold: quantity_sold value
        :return: search objects
        """
        return self._session.query(SoldSnacks).filter(SoldSnacks.quantity_sold == quantity_sold).order_by(SoldSnacks.quantity_sold.desc()).all()
