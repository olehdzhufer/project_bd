from t08_flask_mysql.app.my_project.auth.dao import coins_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class CoinsService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = coins_dao
