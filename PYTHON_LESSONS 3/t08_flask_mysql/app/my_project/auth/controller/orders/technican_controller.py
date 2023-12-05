from t08_flask_mysql.app.my_project.auth.service import technican_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class TechnicanController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = technican_service