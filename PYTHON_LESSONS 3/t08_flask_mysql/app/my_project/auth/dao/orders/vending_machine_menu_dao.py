from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import VendingMachineMenu


class VendingMachineMenuDAO(GeneralDAO):
    """
    Realisation of Vending Machine Menu data access layer.
    """
    _domain_type = VendingMachineMenu

    def find_by_vending_machine_id(self, vending_machines_id: int) -> List[object]:
        """
        Gets Vending Machine Menu objects from the database table by field 'vending_machines_id'.
        :param vending_machines_id: vending_machines_id value
        :return: search objects
        """
        return self._session.query(VendingMachineMenu).filter(VendingMachineMenu.vending_machines_id == vending_machines_id).order_by(VendingMachineMenu.vending_machines_id).all()
