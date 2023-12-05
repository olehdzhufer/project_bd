from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Coins(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "coins"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    coin_loading_date = db.Column(db.Date, nullable=False)
    coin_amount = db.Column(db.Integer, nullable=False)

    vending_machines = db.relationship('CoinsHasVendingMachines', back_populates='coin')


    def __repr__(self) -> str:
        return f"Coins({self.id}, '{self.coin_loading_date}', '{self.coin_amount}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "coin_loading_date": self.coin_loading_date,
            "coin_amount": self.coin_amount,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Coins:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Coins(
            coin_loading_date=dto_dict.get("coin_loading_date"),
            coin_amount=dto_dict.get("coin_amount"),
        )
        return obj
