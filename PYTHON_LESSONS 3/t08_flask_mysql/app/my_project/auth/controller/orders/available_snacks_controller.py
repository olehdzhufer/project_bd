from t08_flask_mysql.app.my_project.auth.service import available_snacks_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class AvailableSnacksController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = available_snacks_service

