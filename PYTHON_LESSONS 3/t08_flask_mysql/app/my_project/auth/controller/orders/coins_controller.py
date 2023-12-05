from t08_flask_mysql.app.my_project.auth.service import coins_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CoinsController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = coins_service
