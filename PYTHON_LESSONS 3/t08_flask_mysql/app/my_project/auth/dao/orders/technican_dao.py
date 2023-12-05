from typing import List

from t08_flask_mysql.app.my_project.auth.dao.general_dao import GeneralDAO
from t08_flask_mysql.app.my_project.auth.domain import Technican


class TechnicanDAO(GeneralDAO):
    """
    Realisation of Technichan data access layer.
    """
    _domain_type = Technican

    def find_by_name(self, name: str) -> List[object]:
        """
        Gets Technichan objects from the database table by field 'name'.
        :param name: name value
        :return: search objects
        """
        return self._session.query(Technican).filter(Technican.name == name).order_by(Technican.name).all()
