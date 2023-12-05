from __future__ import annotations
from typing import Dict, Any


from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class VendingMachineMenu(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "vending_machine_menu"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vending_machine_id = db.Column(db.Integer, nullable=False)



    def __repr__(self) -> str:
        return f"VendingMachineMenu({self.id}, {self.vending_machines_id})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "vending_machines_id": self.vending_machines_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> VendingMachineMenu:
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = VendingMachineMenu(
            vending_machines_id=dto_dict.get("vending_machines_id"),
        )
        return obj
