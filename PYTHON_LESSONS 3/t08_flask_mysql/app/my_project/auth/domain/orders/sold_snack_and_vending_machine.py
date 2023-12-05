class SoldSnackAndVendingMachine:
    def __init__(self, sale_data, quantity_sold, address, gps_coordinates, last_loading_date):
        self.sale_data = sale_data
        self.quantity_sold = quantity_sold
        self.address = address
        self.gps_coordinates = gps_coordinates
        self.last_loading_date = last_loading_date

    def to_dict(self):
        return {
            "sale_data": self.sale_data,
            "quantity_sold": self.quantity_sold,
            "address": self.address,
            "gps_coordinates": self.gps_coordinates,
            "last_loading_date": self.last_loading_date,

        }