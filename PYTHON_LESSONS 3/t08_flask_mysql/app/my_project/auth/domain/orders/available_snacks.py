from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class AvailableSnacks(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "available_snacks"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    current_quantity = db.Column(db.String(45), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    product = db.relationship("Product", backref="available_snacks") # only on the child class

    def __repr__(self) -> str:
        return f"AvailableSnacks({self.id}, '{self.current_quantity}', '{self.product_id}')"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO without relationship
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "current_quantity": self.current_quantity,
            "product_id": self.product_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> AvailableSnacks:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = AvailableSnacks(
            current_quantity=dto_dict.get("current_quantity"),
            product_id=dto_dict.get("product_id"),
        )
        return obj

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the object to a dictionary for JSON serialization.
        :return: Dictionary representation of the object
        """
        return {
            "id": self.id,
            # інші поля
        }