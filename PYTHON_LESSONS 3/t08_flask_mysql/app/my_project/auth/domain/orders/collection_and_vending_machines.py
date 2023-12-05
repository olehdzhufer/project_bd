class CollectionAndVendingMachine:
    def __init__(self, collection_date, collected__amount, address, gps_coordinates, last_loading_date):
        self.collection_date = collection_date
        self.collected__amount = collected__amount
        self.address = address
        self.gps_coordinates = gps_coordinates
        self.last_loading_date = last_loading_date



    def to_dict(self):
        return {
            "collection_date": self.collection_date,
            "collected__amount": self.collected__amount,
            "address": self.address,
            "gps_coordinates": self.gps_coordinates,
            "last_loading_date": self.last_loading_date,
        }