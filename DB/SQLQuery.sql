CREATE TABLE menu (
    id INT IDENTITY(1,1) PRIMARY KEY,
    name NVARCHAR(100) NOT NULL,
    price FLOAT NOT NULL,
    type NVARCHAR(50) NOT NULL
)

CREATE TABLE orders (
    id INT IDENTITY(1,1) PRIMARY KEY,
    item_id INT NOT NULL,
    item_name NVARCHAR(100) NOT NULL
);

INSERT INTO menu (name, price, type) VALUES
('Espresso', 2.50, 'Drink'),
('Cappuccino', 3.00, 'Drink'),
('Latte', 3.50, 'Drink'),
('Americano', 2.75, 'Drink'),
('Mocha', 3.25, 'Drink'),
('Flat White', 3.00, 'Drink'),
('Macchiato', 2.80, 'Drink'),
('Iced Coffee', 3.10, 'Drink'),
('Cold Brew', 3.20, 'Drink'),
('Green Tea', 2.25, 'Drink'),

('Black Tea', 2.00, 'Drink'),
('Herbal Tea', 2.50, 'Drink'),
('Milkshake', 3.75, 'Drink'),
('Hot Chocolate', 3.00, 'Drink'),
('Orange Juice', 3.00, 'Drink'),
('Lemonade', 2.50, 'Drink'),
('Water Bottle', 1.00, 'Drink'),
('Soda', 1.50, 'Drink'),
('Iced Latte', 3.40, 'Drink'),
('Chai Latte', 3.20, 'Drink'),

('Cheesecake', 4.00, 'Food'),
('Chocolate Muffin', 2.00, 'Food'),
('Croissant', 2.20, 'Food'),
('Donut', 1.80, 'Food'),
('Brownie', 2.75, 'Food'),
('Bagel with Cream Cheese', 3.25, 'Food'),
('Turkey Sandwich', 5.50, 'Food'),
('Ham & Cheese Sandwich', 5.00, 'Food'),
('Veggie Wrap', 4.75, 'Food'),
('Chicken Panini', 6.00, 'Food'),

('Salad Bowl', 4.50, 'Food'),
('Fruit Cup', 2.50, 'Food'),
('Granola Bar', 1.50, 'Food'),
('Yogurt Parfait', 3.00, 'Food'),
('Pancakes', 4.00, 'Food'),
('French Toast', 4.25, 'Food'),
('Omelette', 5.25, 'Food'),
('Scrambled Eggs', 3.50, 'Food'),
('Toasted Bread', 1.20, 'Food'),
('Butter Croissant', 2.40, 'Food'),

('Chocolate Cake', 4.50, 'Food'),
('Apple Pie', 3.80, 'Food'),
('Blueberry Muffin', 2.10, 'Food'),
('Spinach Quiche', 4.75, 'Food'),
('Tuna Sandwich', 5.25, 'Food'),
('Egg Salad Sandwich', 4.80, 'Food'),
('Cinnamon Roll', 2.60, 'Food'),
('Peanut Butter Toast', 2.90, 'Food'),
('Avocado Toast', 3.75, 'Food'),
('Mixed Nuts', 2.20, 'Food');


select * from menu

select * from orders

delete from orders where id in (21,22)

delete from menu

grant select, insert, update, delete on menu to coffee_admin123

grant select, insert, update, delete on orders to coffee_admin123