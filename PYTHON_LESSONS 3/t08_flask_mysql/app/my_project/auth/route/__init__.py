"""
2023
apavelchak@gmail.com
© Andrii Pavelchak
"""

from flask import Flask

from .error_handler import err_handler_bp


def register_routes(app: Flask) -> None:
    """
    Registers all necessary Blueprint routes
    :param app: Flask application object
    """
    app.register_blueprint(err_handler_bp)

    from .orders.client_route import client_bp
    from .orders.sold_snacks_route import sold_snacks_bp
    from .orders.available_snacks_route import available_snacks_bp
    from .orders.coins_route import coins_bp
    from .orders.collection_route import collection_bp
    from .orders.technican_route import technican_bp
    from .orders.vending_machine_route import vending_machine_bp
    from .orders.product_route import product_bp
    from .orders.vending_machine_menu_route import vending_machine_menu_bp

    app.register_blueprint(client_bp)
    app.register_blueprint(sold_snacks_bp)
    app.register_blueprint(available_snacks_bp)
    app.register_blueprint(coins_bp)
    app.register_blueprint(collection_bp)
    app.register_blueprint(technican_bp)
    app.register_blueprint(vending_machine_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(vending_machine_menu_bp)
