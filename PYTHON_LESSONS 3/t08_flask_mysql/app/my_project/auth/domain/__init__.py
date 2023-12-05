
# Import here Domain Class that are needed for ORM
# orders DB
from t08_flask_mysql.app.my_project.auth.domain.orders.client import Client
from t08_flask_mysql.app.my_project.auth.domain.orders.sold_snacks import SoldSnacks
from t08_flask_mysql.app.my_project.auth.domain.orders.available_snacks import AvailableSnacks
from t08_flask_mysql.app.my_project.auth.domain.orders.coins import Coins
from t08_flask_mysql.app.my_project.auth.domain.orders.collection import Collection
from t08_flask_mysql.app.my_project.auth.domain.orders.technican import Technican
from t08_flask_mysql.app.my_project.auth.domain.orders.vending_machine import VendingMachine
from t08_flask_mysql.app.my_project.auth.domain.orders.product import Product
from t08_flask_mysql.app.my_project.auth.domain.orders.vending_machine_menu import VendingMachineMenu
from .orders.sold_snacks_has_vending_machines import SoldSnacksHasVendingMachines
from .orders.technican_has_vending_machines import TechnicanHasVendingMachines
from .orders.coins_has_vending_machines import CoinsHasVendingMachines
from .orders.collection_has_vending_machines import CollectionHasVendingMachines
