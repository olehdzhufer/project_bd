from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class SoldSnacks(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "sold_snacks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sale_data = db.Column(db.Date, nullable=False)
    quantity_sold = db.Column(db.Integer, nullable=False)

    vending_machines = db.relationship('SoldSnacksHasVendingMachines', back_populates='snack')

    def __repr__(self) -> str:
        return f"SoldSnacks({self.id}, '{self.sale_data}', '{self.quantity_sold}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "sale_data": str(self.sale_data),
            "quantity_sold": self.quantity_sold,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SoldSnacks:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = SoldSnacks(
            sale_data=dto_dict.get("sale_data"),
            quantity_sold=dto_dict.get("quantity_sold"),
        )
        return obj
