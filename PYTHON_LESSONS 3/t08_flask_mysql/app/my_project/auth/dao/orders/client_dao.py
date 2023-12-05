"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Client
from t08_flask_mysql.app.my_project.auth.domain.orders.sold_snacks import SoldSnacks


class ClientDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Client

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Client objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.name == name).order_by(Client.name).all()

    def find_by_number(self, number: int) -> List[object]:
        """
        Gets Client objects from database table by field 'number'.
        :param number: number value
        :return: search objects
        """
        return self._session.query(Client).filter(Client.number == number).order_by(Client.number.desc()).all()

    def get_all(self) -> List[object]:
        """
        Gets all Sold Snacks objects from the database table.
        :return: all Sold Snacks objects
        """
        return self._session.query(SoldSnacks).all()