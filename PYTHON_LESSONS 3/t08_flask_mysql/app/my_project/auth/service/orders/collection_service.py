from t08_flask_mysql.app.my_project.auth.dao import collection_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class CollectionService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = collection_dao
