from typing import Dict, Any

from t08_flask_mysql.app.my_project import db
from t08_flask_mysql.app.my_project.auth.domain.i_dto import IDto


class Product(db.Model, IDto):
    """
    Model declaration for Data Mapper.
    """
    __tablename__ = "product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    vending_machine_menu_id = db.Column(db.Integer,db.ForeignKey('vending_machine_menu.id') ,nullable=False)
    name = db.Column(db.String(45), nullable=False)
    brand = db.Column(db.String(45), nullable=True)
    price = db.Column(db.Integer, nullable=False)
    vending_machine_menu = db.relationship("VendingMachineMenu", backref="product")

    def __repr__(self) -> str:
        return f"Product({self.id}, {self.vending_machine_menu_id}, '{self.name}', '{self.brand}', {self.price})"

    def put_into_dto(self) -> Dict[str, Any]:
        """
        Puts domain object into DTO
        :return: DTO object as dictionary
        """
        return {
            "id": self.id,
            "vending_machine_menu_id": self.vending_machine_menu_id,
            "name": self.name,
            "brand": self.brand,
            "price": self.price,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> 'Product':
        """
        Creates domain object from DTO
        :param dto_dict: DTO object
        :return: Domain object
        """
        obj = Product(
            vending_machine_menu_id=dto_dict.get("vending_machine_menu_id"),
            name=dto_dict.get("name"),
            brand=dto_dict.get("brand"),
            price=dto_dict.get("price"),
        )
        return obj
