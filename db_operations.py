import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Centralized connection logic."""
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="your_password",
        database="mydata"
    )

def initialize_system():
    """Creates tables if they don't exist."""
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # 1. Packages Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS packages (
            id INT AUTO_INCREMENT PRIMARY KEY,
            order_id VARCHAR(255) NOT NULL,
            destination VARCHAR(255),
            driver_id VARCHAR(255) NOT NULL,
            vehicle_no VARCHAR(20),
            status VARCHAR(50) DEFAULT 'Pending',
            customer_id INT
        )
    """)
    
    # 2. Drivers Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS drivers (
            id INT AUTO_INCREMENT PRIMARY KEY,
            driver_name VARCHAR(255) NOT NULL,
            license_no VARCHAR(50),
            contact_no VARCHAR(15) NOT NULL
        )
    """)
    
    # 3. Vehicles Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS vehicles (
            id INT AUTO_INCREMENT PRIMARY KEY,
            plate_no VARCHAR(20),
            status VARCHAR(50) DEFAULT 'Available'
        )
    """)
    
    conn.commit()
    conn.close()

# --- VEHICLE OPERATIONS ---

def add_vehicle(plate_no):
    conn = get_db_connection()
    try:
        cursor = conn.cursor() # Fixed: .cursor() instead of .connect()
        sql = "INSERT INTO vehicles (plate_no) VALUES (%s)"
        cursor.execute(sql, (plate_no,)) # Fixed: Added trailing comma
        conn.commit() # Fixed: Added commit
        return True
    except Error as e:
        print(f"Database Error: {e}")
        return False
    finally:
        conn.close()

# --- DRIVER OPERATIONS ---

def add_driver(driver_name, license_no, contact_no):
    conn = get_db_connection()
    try:
        cursor = conn.cursor() # Fixed: .cursor()
        sql = "INSERT INTO drivers (driver_name, license_no, contact_no) VALUES (%s, %s, %s)"
        cursor.execute(sql, (driver_name, license_no, contact_no))
        conn.commit() # Fixed: Added commit
        return True
    except Error as e:
        print(f"Database Error: {e}")
        return False
    finally:
        conn.close()

# --- DELIVERY OPERATIONS ---

def add_delivery(order_id, destination, driver_id, vehicle_no):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        sql = """
            INSERT INTO packages (order_id, destination, driver_id, vehicle_no) 
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(sql, (order_id, destination, driver_id, vehicle_no))
        conn.commit()
        return cursor.lastrowid 
    except Error as e:
        print(f"Database Error: {e}")
    finally:
        conn.close()

def get_all_deliveries():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT id, order_id, destination, driver_id, vehicle_no, status FROM packages"
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(f"Database Error: {e}")
    finally:
        conn.close()

def update_delivery_status(package_id, new_status):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        sql = "UPDATE packages SET status = %s WHERE id = %s"
        cursor.execute(sql, (new_status, package_id))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Database Error: {e}")
        return False
    finally:
        conn.close()

def delete_delivery(package_id):
    conn = get_db_connection()
    try:
        cursor = conn.cursor()
        sql = "DELETE FROM packages WHERE id = %s"
        cursor.execute(sql, (package_id,))
        conn.commit()
        return cursor.rowcount > 0
    except Error as e:
        print(f"Database Error: {e}")
        return False
    finally:
        conn.close()