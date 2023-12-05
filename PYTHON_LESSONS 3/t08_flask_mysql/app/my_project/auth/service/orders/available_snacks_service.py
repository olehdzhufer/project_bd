from t08_flask_mysql.app.my_project.auth.dao import available_snacks_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class AvailableSnacksService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = available_snacks_dao
