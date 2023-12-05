from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Technican(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "technichan"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    vending_machines = db.relationship('TechnicanHasVendingMachines', back_populates='technican')

    def __repr__(self) -> str:
        return f"Technichan({self.id}, '{self.name}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "name": self.name,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Technican:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Technican(
            name=dto_dict.get("name"),
        )
        return obj
