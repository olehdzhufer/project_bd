class CoinsAndVendingMachine:
    def __init__(self, coin_loading_date, coin_amount, address, gps_coordinates, last_loading_date):
        self.coin_loading_date = coin_loading_date
        self.coin_amount = coin_amount
        self.address = address
        self.gps_coordinates = gps_coordinates
        self.last_loading_date = last_loading_date



    def to_dict(self):
        return {
            "coin_loading_date": self.coin_loading_date,
            "coin_amount": self.coin_amount,
            "address": self.address,
            "gps_coordinates": self.gps_coordinates,
            "last_loading_date": self.last_loading_date,
        }