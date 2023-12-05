from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Coins
from t08_flask_mysql.app.my_project.auth.domain.orders.coins import Coins


class CoinsDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Coins

    def find_by_coin_loading_date(self, coin_loading_date: str) -> List[object]:
        """
        Gets Client objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Coins).filter(Coins.coin_loading_date == coin_loading_date).order_by(Coins.coin_loading_date).all()

    def find_by_coin_amount(self, coin_amount: int) -> List[object]:
        """
        Gets Client objects from database table by field 'number'.
        :param number: number value
        :return: search objects
        """
        return self._session.query(Coins).filter(Coins.coin_amount == coin_amount).order_by(Coins.coin_amount.desc()).all()

