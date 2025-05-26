import csv
from Pagination_class import Pagination
import pyodbc
import os

"""
def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=localhost,1433;'
        'DATABASE=CoffeeShop_db;'
        'UID=coffee_admin123;'
        'PWD=123'
    )
    return conn

    
'SERVER=host.docker.internal,1433'

def get_db_connection():
    server = os.getenv("DB_SERVER")
    database = os.getenv("DB_NAME")
    username = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")

    conn_str = (
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={username};"
        f"PWD={password}"
    )
    return pyodbc.connect(conn_str)

    def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={os.environ["DB_SERVER"]},1433;'
        f'DATABASE={os.environ["DB_NAME"]};'
        f'UID={os.environ["DB_USER"]};'
        f'PWD={os.environ["DB_PASSWORD"]}'
    )
    return conn

    'SERVER=host.docker.internal,1433;'
"""

def get_db_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        f'SERVER={os.environ["DB_SERVER"]},1433;'
        f'DATABASE={os.environ["DB_NAME"]};'
        f'UID={os.environ["DB_USER"]};'
        f'PWD={os.environ["DB_PASSWORD"]}'
    )
    return conn


class CoffeeShop:
    
    def __init__(self, coffee_name):
        """Initialize attributes to describe the Coffee Shop"""
        self.coffee_name = coffee_name
        self.conn = get_db_connection()
        self.menu_dict = self.load_menu_from_db()
        self.orders_list = self.load_orders_from_db()
        

    #=========================================== Menu =====================================================
    def load_menu_from_db(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, price, type FROM menu")
        rows = cursor.fetchall()
        menu = []
        for row in rows:
            menu.append({
                "id": row.id,
                "name": row.name,
                "price": row.price,
                "type": row.type
            })
        return menu
    
    #------------------------------------------------------------------
    def save_menu_to_db(self):
        """
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM menu")
        for item in self.menu_dict:
            cursor.execute(
                "INSERT INTO menu (name, price, type) VALUES (?, ?, ?)",
                item['name'], item['price'], item['type']
            )
        self.conn.commit()
        """
        cursor = self.conn.cursor()
        
        existing_ids = [row.id for row in cursor.execute("SELECT id FROM menu")]
        existing_ids_set = set(existing_ids)
        new_ids_set = set(item['id'] for item in self.menu_dict if 'id' in item)

        ids_to_delete = existing_ids_set - new_ids_set
        for id_to_delete in ids_to_delete:
            cursor.execute("DELETE FROM menu WHERE id = ?", id_to_delete)

        for item in self.menu_dict:
            if 'id' in item and item['id'] in existing_ids_set:
                # Update
                cursor.execute(
                    """
                    UPDATE menu
                    SET name = ?, price = ?, type = ?
                    WHERE id = ?
                    """, 
                    item['name'], item['price'], item['type'], item['id'])
            else:
                # Insert
                cursor.execute(
                    """
                    INSERT INTO menu (name, price, type)
                    VALUES (?, ?, ?)
                    """,
                    item['name'], item['price'], item['type'])

        self.conn.commit()


    #------------------------------------------------------------------
    def menu_view(self):
        print(self.menu_dict)

    #------------------------------------------------------------------
    def menu_by_pagination(self, page_size=5):
        #self.load_menu_from_csv()
        return Pagination(self.menu_dict, page_size)
    
    def get_paginated_menu(self, page, page_size):
        start = (page - 1) * page_size
        end = start + page_size
        return self.menu_dict[start:end]


    #------------------------------------------------------------------
    def menu_add_item(self, new_item): 
        cursor = self.conn.cursor()
        cursor.execute(
            "INSERT INTO menu (name, price, type) VALUES (?, ?, ?)",
            new_item['name'], new_item['price'], new_item['type']
        )
        self.conn.commit()
        self.menu_dict = self.load_menu_from_db()
        return "Item added successfully"
    
    #------------------------------------------------------------------
    def menu_edit_item_price(self, item_id, new_price):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE menu SET price = ? WHERE id = ?",
            new_price, item_id
        )
        self.conn.commit()
        self.menu_dict = self.load_menu_from_db()
        return f"Price for item {item_id} updated"
    
    #------------------------------------------------------------------
    def menu_delete_item(self, item_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM menu WHERE id = ?", item_id)
        self.conn.commit()
        self.menu_dict = self.load_menu_from_db()
        return f"Item with ID {item_id} deleted"
        
        
    #------------------------------------------------------------------
    def cheapest_item_list(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, price, type FROM menu ORDER BY price ASC")
        rows = cursor.fetchall()
        return [{"id": row.id, "name": row.name, "price": row.price, "type": row.type} for row in rows]

    #------------------------------------------------------------------
    def drinks_only(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, price, type FROM menu WHERE type = 'drink'")
        rows = cursor.fetchall()
        return [{"id": row.id, "name": row.name, "price": row.price, "type": row.type} for row in rows]

    #------------------------------------------------------------------
    def food_only(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, name, price, type FROM menu WHERE type = 'food'")
        rows = cursor.fetchall()
        return [{"id": row.id, "name": row.name, "price": row.price, "type": row.type} for row in rows]


    #=============================================== Order ==================================================
    def load_orders_from_db(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT item_id, item_name FROM orders ORDER BY id")
        rows = cursor.fetchall()
        self.orders_list = [{'item_id': row.item_id, 'item_name': row.item_name} for row in rows]
        return self.orders_list

    #------------------------------------------------------------------
    def save_orders_to_db(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM orders")
        for order in self.orders_list:
            cursor.execute(
                "INSERT INTO orders (item_id, item_name) VALUES (?, ?)",
                order['item_id'], order['item_name']
            )
        self.conn.commit()


    #------------------------------------------------------------------
    def add_order(self, item_name):
        """Adds the name of the item to the end of the orders list if it exists on the menu"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT id FROM menu WHERE name = ?", item_name)
        result = cursor.fetchone()
        if result:
            item_id = result.id
            cursor.execute("INSERT INTO orders (item_id, item_name) VALUES (?, ?)", item_id, item_name)
            self.conn.commit()

            self.orders_list.append({'item_id': item_id, 'item_name': item_name})
            self.save_orders_to_db()

            return f"Order added: {item_name}"
        else:
            return "Item not found in menu"
    
    #------------------------------------------------------------------
    def list_orders(self):
        """Returns the item names of the orders taken"""
        orders = self.load_orders_from_db
        return [{"id": order['item_id'], "name":order['item_name']} for order in orders]
        ##return [self.list_orders]
        ##[{"id": row.id, "name": row.name, "price": row.price, "type": row.type} for row in rows]



    #------------------------------------------------------------------
    def fulfill_order(self):
        """Return the ready item in the list orders"""
        cursor = self.conn.cursor()
        cursor.execute("SELECT TOP 1 id FROM orders ORDER BY id ASC")
        row = cursor.fetchone()
        if row:
            cursor.execute("DELETE FROM orders WHERE id = ?", row.id)
            self.conn.commit()

            self.orders_list.pop(0)
            self.save_orders_to_db()


    #------------------------------------------------------------------
    def due_amount(self):
        """Returns the total amount due for the orders taken"""
        cursor = self.conn.cursor()
        ##cursor.execute("SELECT SUM(price) FROM orders")
        cursor.execute("""
            SELECT SUM(menu.price) AS total
            FROM orders
            JOIN menu ON orders.item_id = menu.id
        """)
        row = cursor.fetchone()
        return row.total if row.total else 0.0
    #=======================================================================================================

