from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Collection


class CollectionDAO(GeneralDAO):
    """
    Realisation of Client data access layer.
    """
    _domain_type = Collection

    def find_by_collection_date(self, collection_date: str) -> List[object]:
        """
        Gets Client objects from database table by field name.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Collection).filter(Collection.collection_date == collection_date).order_by(Collection.coin_loading_date).all()

    def find_by_collected__amount(self, collected__amount: int) -> List[object]:
        """
        Gets Client objects from database table by field 'number'.
        :param number: number value
        :return: search objects
        """
        return self._session.query(Collection).filter(Collection.collected__amount == collected__amount).order_by(Collection.collected__amount.desc()).all()

