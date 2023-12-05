"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

# orders DB
from .orders.client_dao import ClientDAO
from .orders.sold_snacks_dao import SoldSnacksDAO
from .orders.available_snacks_dao import AvailableSnacksDAO
from .orders.coins_dao import CoinsDAO
from .orders.collection_dao import CollectionDAO
from .orders.technican_dao import TechnicanDAO
from .orders.vending_machine_dao import VendingMachineDAO
from .orders.product_dao import ProductDAO
from .orders.vending_machine_menu_dao import VendingMachineMenuDAO

client_dao = ClientDAO()
sold_snacks_dao = SoldSnacksDAO()
available_snacks_dao = AvailableSnacksDAO()
coins_dao = CoinsDAO()
collection_dao = CollectionDAO()
technican_dao = TechnicanDAO()
vending_machine_dao = VendingMachineDAO()
product_dao = ProductDAO()
vending_machine_menu_dao = VendingMachineMenuDAO()

