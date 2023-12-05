from t08_flask_mysql.app.my_project.auth.dao import technican_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class TechnicanService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = technican_dao