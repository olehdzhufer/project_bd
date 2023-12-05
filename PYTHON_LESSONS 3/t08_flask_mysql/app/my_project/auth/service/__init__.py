"""
2022
apavelchak@gmail.com
© Andrii Pavelchak
"""

from .orders.client_service import ClientService
from .orders.sold_snacks_service import SoldSnacksService
from .orders.available_snacks_service import AvailableSnacksService
from .orders.coins_service import CoinsService
from .orders.collection_service import CollectionService
from .orders.technican_service import TechnicanService
from .orders.vending_machine_service import VendingMachineService
from .orders.product_service import ProductService
from .orders.vending_machine_menu_service import VendingMachineMenuService

client_service = ClientService()
sold_snacks_service = SoldSnacksService()
available_snacks_service = AvailableSnacksService()
coins_service = CoinsService()
collection_service = CollectionService()
technican_service = TechnicanService()
vending_machine_service = VendingMachineService()
product_service = ProductService()
vending_machine_menu_service = VendingMachineMenuService()
