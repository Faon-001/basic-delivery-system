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
    def __init__(self):
        self.orders = {}
        self.tracking_sessions = {}

    def create_order(self, order_id, item, dest):
        new_order = Order(order_id, item, dest)
        self.orders[order_id] = new_order
        print(f"System: Order {order_id} created.")

    def dispatch(self, order_id, driver, vehicle):
        if order_id in self.orders and vehicle.is_available:
            # Link them up
            order = self.orders[order_id]
            driver.active_vehicle = vehicle
            vehicle.is_available = False
            order.status = "Out for Delivery"
            
            # Start Tracking
            self.tracking_sessions[order_id] = Tracking(order_id)
            print(f"System: {driver.name} is delivering {order.item} via {vehicle.model}")
        else:
            print("Dispatch Error: Order not found or vehicle unavailable.")

# --- QUICK SIMULATION ---
manager = DeliveryManager()
van_01 = Vehicle("ABC-123", "Ford Transit")
driver_joe = Driver(1, "Joe")

# 1. Create an order
manager.create_order(101, "Coffee Machine", "456 Oak St")

# 2. Dispatch the order
manager.dispatch(101, driver_joe, van_01)

# 3. Track movement
manager.tracking_sessions[101].record_movement(40.7128, -74.0060)