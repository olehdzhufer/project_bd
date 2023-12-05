from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Collection(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "collection"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    collection_date = db.Column(db.Date, nullable=False)
    collected__amount = db.Column(db.Integer, nullable=False)

    vending_machines = db.relationship('CollectionHasVendingMachines', back_populates='collection')


    def __repr__(self) -> str:
        return f"Collection({self.id}, '{self.collection_date}', '{self.collected_amount}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "collection_date": self.collection_date,
            "collected__amount": self.collected__amount,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Collection:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Collection(
            collection_date=dto_dict.get("collection_date"),
            collected__amount=dto_dict.get("collected__amount"),
        )
        return obj
