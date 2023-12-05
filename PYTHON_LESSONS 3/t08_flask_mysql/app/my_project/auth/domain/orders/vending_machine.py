from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class VendingMachine(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "vending_machines"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    address = db.Column(db.String(45), nullable=False)
    gps_coordinates = db.Column(db.String(45), nullable=False)
    last_loading_date = db.Column(db.Date, nullable=False)

    sold_snacks = db.relationship('SoldSnacksHasVendingMachines', back_populates='vending_machine')
    technican = db.relationship('TechnicanHasVendingMachines', back_populates='vending_machine')
    coins = db.relationship('CoinsHasVendingMachines', back_populates='vending_machine')
    collection = db.relationship('CollectionHasVendingMachines', back_populates='vending_machine')

    def __repr__(self) -> str:
        return f"VendingMachine({self.id}, '{self.address}', '{self.gps_coordinates}', '{self.last_loading_date}')"


    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "address": self.address,
            "gps_coordinates": self.gps_coordinates,
            "last_loading_date": str(self.last_loading_date),
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> VendingMachine:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = VendingMachine(
            address=dto_dict.get("address"),
            gps_coordinates=dto_dict.get("gps_coordinates"),
            last_loading_date=dto_dict.get("last_loading_date"),
        )
        return obj
