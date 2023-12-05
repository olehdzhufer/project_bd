from __future__ import annotations
from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class TechnicanHasVendingMachines(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "technichan_has_vending_machines"
    technichan_id = db.Column(db.Integer, db.ForeignKey('technichan.id'), primary_key=True)
    vending_machines_id = db.Column(db.Integer, db.ForeignKey('vending_machines.id'), primary_key=True)

    technican = db.relationship('Technican', back_populates='vending_machines')
    vending_machine = db.relationship('VendingMachine', back_populates='technican')

    def __repr__(self) -> str:
        return f"<TechnicanHasVendingMachines(technichan_id={self.technichan_id}, vending_machines_id={self.vending_machines_id})>"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {

        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> TechnicanHasVendingMachines:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = TechnicanHasVendingMachines(

        )
        return obj
