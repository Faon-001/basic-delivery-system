import datetime

class Order:
    def __init__(self, order_id, item, destination):
        self.order_id = order_id
        self.item = item
        self.destination = destination
        self.status = "Pending"

class Vehicle:
    def __init__(self, plate_no, model):
        self.plate_no = plate_no
        self.model = model
        self.is_available = True

class Driver:
    def __init__(self, driver_id, name):
        self.driver_id = driver_id
        self.name = name
        self.active_vehicle = None

class Tracking:
    def __init__(self, order_id):
        self.order_id = order_id
        self.location_log = []
        
    def record_movement(self, lat, lng):
        timestamp = datetime.datetime.now().strftime("%H:%M:%S")
        self.location_log.append({"time": timestamp, "coords": (lat, lng)})
        print(f"Tracking Order {self.order_id}: Moved to {lat}, {lng}")

class DeliveryManager:
    print("hello")