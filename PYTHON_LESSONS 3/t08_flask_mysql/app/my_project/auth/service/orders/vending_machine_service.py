from t08_flask_mysql.app.my_project.auth.dao import vending_machine_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class VendingMachineService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = vending_machine_dao