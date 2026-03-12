import db_operations as db

class DeliveryManager:
    def __init__(self):
        db.initialize_system()

    def run(self):
        while True:
            print("\n--- Delivery Management Software ---")
            print("1. Add a delivery")
            print("2. Add a new vehicle")
            print("3. Add a new driver")
            print("4. View all deliveries")
            print("5. Exit")
            
            try:
                choice = int(input("\nSelect an option: "))
            except ValueError:
                print("Please enter a valid number.")
                continue

            match choice:
                case 1:
                    self.take_delivery()
                case 2:
                    self.add_new_vehicle()
                case 3:
                    self.add_new_driver()
                case 4:
                    self.show_deliveries()
                case 5:
                    print("Exiting...")
                    break
                case _:
                    print("Invalid option.")

    def take_delivery(self):
        oid = input("Enter the order id: ")
        dest = input("Enter the destination: ")
        did = input("Enter the driver id: ")
        pno = input("Enter plate number: ")
        
        # Now we call the worker function from db_operations
        db.add_delivery(oid, dest, did, pno)
        print("Delivery added successfully!")

    def add_new_vehicle(self):
        pno = input("Enter plate number: ")
        db.add_vehicle(pno)
        print("Vehicle registered!")

    def add_new_driver(self):
        name = input("Driver Name: ")
        lic = input("License No: ")
        con = input("Contact No: ")
        db.add_driver(name, lic, con)
        print("Driver registered!")
        
    def show_deliveries(self):
        data = db.get_all_deliveries()
        print("\n--- Current Deliveries ---")
        for row in data:
            print(f"Order: {row['order_id']} | Dest: {row['destination']} | Status: {row['status']}")

# This is the "Entry Point" of your program
if __name__ == "__main__":
    manager = DeliveryManager()
    manager.run()