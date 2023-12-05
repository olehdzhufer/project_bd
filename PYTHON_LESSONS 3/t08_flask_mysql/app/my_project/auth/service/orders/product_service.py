from t08_flask_mysql.app.my_project.auth.dao import product_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class ProductService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = product_dao