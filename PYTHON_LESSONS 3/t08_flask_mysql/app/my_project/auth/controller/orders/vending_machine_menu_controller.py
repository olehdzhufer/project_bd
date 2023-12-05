from t08_flask_mysql.app.my_project.auth.service import vending_machine_menu_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class VendingMachineMenuController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = vending_machine_menu_service