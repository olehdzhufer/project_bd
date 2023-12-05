from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class SoldSnacksHasVendingMachines(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "sold_snacks_has_vending_machines"
    sold_snacks_id = db.Column(db.Integer, db.ForeignKey('sold_snacks.id'), primary_key=True)
    vending_machines_id = db.Column(db.Integer, db.ForeignKey('vending_machines.id'), primary_key=True)

    snack = db.relationship('SoldSnacks', back_populates='vending_machines')
    vending_machine = db.relationship('VendingMachine', back_populates='sold_snacks')

    def __repr__(self) -> str:
        return f"<SoldSnacksHasVendingMachines(sold_snacks_id={self.sold_snacks_id}, vending_machines_id={self.vending_machines_id})>"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> SoldSnacksHasVendingMachines:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = SoldSnacksHasVendingMachines(

        )
        return obj
