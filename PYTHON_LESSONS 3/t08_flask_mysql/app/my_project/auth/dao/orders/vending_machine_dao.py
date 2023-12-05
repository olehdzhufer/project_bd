from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import VendingMachine

class VendingMachineDAO(GeneralDAO):
    """
    Realisation of Vending Machines data access layer.
    """
    _domain_type = VendingMachine

    def find_by_address(self, address: str) -> List[object]:
        """
        Gets Vending Machine objects from the database table by field 'address'.
        :param address: address value
        :return: search objects
        """
        return self._session.query(VendingMachine).filter(VendingMachine.address == address).order_by(VendingMachine.address).all()

    def find_by_coordinates(self, gps_coordinates: str) -> List[object]:
        """
        Gets Vending Machine objects from the database table by field 'gps_coordinates'.
        :param gps_coordinates: gps_coordinates value
        :return: search objects
        """
        return self._session.query(VendingMachine).filter(VendingMachine.gps_coordinates == gps_coordinates).order_by(VendingMachine.gps_coordinates).all()

    def find_by_loading_date(self, last_loading_date: str) -> List[object]:
        """
        Gets Vending Machine objects from the database table by field 'last_loading_date'.
        :param last_loading_date: last_loading_date value
        :return: search objects
        """
        return self._session.query(VendingMachine).filter(VendingMachine.last_loading_date == last_loading_date).order_by(VendingMachine.last_loading_date).all()
