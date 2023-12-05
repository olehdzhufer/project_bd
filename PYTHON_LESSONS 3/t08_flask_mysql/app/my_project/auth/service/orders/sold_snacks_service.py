"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from t08_flask_mysql.app.my_project.auth.dao import sold_snacks_dao
from t08_flask_mysql.app.my_project.auth.service.general_service import GeneralService


class SoldSnacksService(GeneralService):
    """
    Realisation of Client service.
    """
    _dao = sold_snacks_dao
