class TechnicanAndVendingMachine:
    def __init__(self, name, address, gps_coordinates,last_loading_date ):
        self.name = name
        self.address = address
        self.gps_coordinates = gps_coordinates
        self.last_loading_date = last_loading_date

    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "gps_coordinates": self.gps_coordinates,
            "last_loading_date": self.last_loading_date,
        }