from t08_flask_mysql.app.my_project.auth.service import collection_service
from t08_flask_mysql.app.my_project.auth.controller.general_controller import GeneralController


class CollectionController(GeneralController):
    """
    Realisation of ClientType controller.
    """
    _service = collection_service