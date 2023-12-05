from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import AvailableSnacks


class AvailableSnacksDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = AvailableSnacks

    def find_by_current_quantity(self, current_quantity):
        return self._session.query(AvailableSnacks).filter(AvailableSnacks.current_quantity == current_quantity).order_by(AvailableSnacks.current_quantity).all()

    def find_by_product_id(self, product_id: int):
        return self._session.query(AvailableSnacks).filter(AvailableSnacks.product_id == product_id).all()
