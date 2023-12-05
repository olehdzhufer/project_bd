"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.client_controller import ClientController
from .orders.sold_snacks_controller import SoldSnacksController
from .orders.available_snacks_controller import AvailableSnacksController
from .orders.coins_controller import CoinsController
from .orders.collection_controller import CollectionController
from .orders.technican_controller import TechnicanController
from .orders.vending_machine_controller import VendingMachineController
from .orders.product_controller import ProductController
from .orders.vending_machine_menu_controller import VendingMachineMenuController

client_controller = ClientController()
sold_snacks_controller = SoldSnacksController()
available_snacks_controller = AvailableSnacksController()
coins_controller = CoinsController()
collection_controller = CollectionController()
technican_controller = TechnicanController()
vending_machine_controller = VendingMachineController()
product_controller = ProductController()
vending_machine_menu_controller = VendingMachineMenuController()