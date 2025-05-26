from flask import Flask, render_template, request, redirect
from CoffeeShop_class import CoffeeShop
from Pagination_class import Pagination
import pyodbc

app = Flask(__name__)

shop = CoffeeShop("Space")
page_size = 10
menu_paginator = shop.menu_by_pagination(page_size=page_size)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu_home():
    shop.menu_dict = shop.load_menu_from_db()
    return render_template('menu.html')

@app.route('/menu/add', methods=['POST'])
def add_menu_item():
    name = request.form['name']
    price = float(request.form['price'])
    type_ = request.form['type']
    shop.menu_add_item({'name': name, 'price': price, 'type': type_})
    shop.save_menu_to_db()
    return redirect('/menu')

@app.route('/menu/edit', methods=['POST'])
def edit_item():
    item_id = int(request.form['id'])
    new_price = float(request.form['price'])
    shop.menu_edit_item_price(item_id, new_price)
    shop.save_menu_to_db()
    return redirect('/menu')

@app.route('/menu/delete', methods=['POST'])
def delete_item():
    item_id = int(request.form['id'])
    shop.menu_delete_item(item_id)
    shop.save_menu_to_db()
    return redirect('/menu')

@app.route('/menu/cheapest')
def cheapest_items():
    items = shop.cheapest_item_list()
    return render_template('menu_result.html', title="Cheapest Items", results=items)

@app.route('/menu/food')
def food_items():
    items = shop.food_only()
    return render_template('menu_result.html', title="Food Items", results=items)

@app.route('/menu/drink')
def drink_items():
    items = shop.drinks_only()
    return render_template('menu_result.html', title="Drink Items", results=items)


@app.route('/menu/view')
@app.route('/menu/page/<int:page>')
def view_menu_paginated(page=1):
    ##shop.menu_dict = shop.load_menu_from_db()
    items = shop.get_paginated_menu(page, page_size)
    total_items = len(shop.menu_dict)
    total_pages = (total_items + page_size - 1) // page_size
    return render_template('menu_page.html', items=items, page=page, total_pages=total_pages)
"""
def view_menu_paginated(page=1):
    paginator = shop.menu_by_pagination(page_size=page_size)
    paginator.start_point = (page - 1) * page_size
    items = paginator.getVisibleItems()
    total_pages = (len(paginator.items) + page_size - 1) // page_size
    return render_template('menu_page.html', items=items, page=page, total_pages=total_pages)
"""

@app.route('/orders')
def orders_home():
    return render_template('orders.html')

@app.route('/orders/add', methods=['POST'])
def add_order():
    item_name = request.form['item']
    shop.add_order(item_name)
    shop.save_orders_to_db()
    return redirect('/orders')

@app.route('/orders/fulfill')
def fulfill_order():
    shop.fulfill_order()
    shop.save_orders_to_db()
    return redirect('/orders')

@app.route('/orders/list')
def list_orders():
    orders = shop.load_orders_from_db()
    return render_template('orders_list.html',title="Orders List", orders=orders)
    ##return f"<pre>{orders}</pre><br><a href='/orders'>Back</a>"


@app.route('/orders/total')
def total_due():
    total = shop.due_amount()
    return f"<h3>Total amount due: ${total:.2f}</h3><br><a href='/orders'>Back</a>"

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)



"""
shop = CoffeeShop("Space", "menu_csv_file.csv", "orders_csv_file.csv")
page_size = 10
#menu_paginator = shop.menu_by_pagination(page_size=page_size)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/menu')
def menu_home():
    return render_template('menu.html')

@app.route('/menu/add', methods=['POST'])
def add_menu_item():
    name = request.form['name']
    price = float(request.form['price'])
    type_ = request.form['type']
    shop.menu_add_item({"name": name, "price": price, "type": type_})
    return redirect('/menu')

@app.route('/menu/edit', methods=['POST'])
def edit_item():
    item_id = int(request.form['id'])
    new_price = float(request.form['price'])
    shop.menu_edit_item_price(item_id, new_price)
    return redirect('/menu')

@app.route('/menu/delete', methods=['POST'])
def delete_item():
    item_id = int(request.form['id'])
    shop.menu_delete_item(item_id)
    return redirect('/menu')

@app.route('/menu/cheapest')
def cheapest_items():
    items = shop.cheapest_item_list()
    return render_template('menu_result.html', title="Cheapest Items", items=items)
    #return f"<pre>{items}</pre><br><a href='/menu'>Back</a>"

@app.route('/menu/food')
def food_items():
    items = shop.food_only()
    return render_template('menu_result.html', title="Food Items", items=items)
    #return f"<pre>{items}</pre><br><a href='/menu'>Back</a>"

@app.route('/menu/drink')
def drink_items():
    items = shop.drinks_only()
    return render_template('menu_result.html', title="Drink Items", items=items)
    #return f"<pre>{items}</pre><br><a href='/menu'>Back</a>"



@app.route('/menu/view')
@app.route('/menu/page/<int:page>')
def view_menu_paginated(page=1):
    items = shop.get_paginated_menu(page, page_size)
    total_pages = (len(shop.menu_dict) + page_size - 1) // page_size
    return render_template('menu_page.html', items=items, page=page, total_pages=total_pages)



@app.route('/orders')
def orders_home():
    return render_template('orders.html')

@app.route('/orders/add', methods=['POST'])
def add_order():
    item = request.form['item']
    shop.add_order(item)
    return redirect('/orders')

@app.route('/orders/fulfill')
def fulfill_order():
    shop.fulfill_order()
    return redirect('/orders')

@app.route('/orders/list')
def list_orders():
    orders = shop.list_orders()
    return f"<pre>{orders}</pre><br><a href='/orders'>Back</a>"

@app.route('/orders/total')
def total_due():
    total = shop.due_amount()
    return f"<h3>Total amount due: ${total:.2f}</h3><br><a href='/orders'>Back</a>"

if __name__ == '__main__':
    app.run(debug=True)
"""