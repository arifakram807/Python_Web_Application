-- Use the schema
USE grocery_store;

-- Create the uom table
CREATE TABLE uom (
    uom_id INT PRIMARY KEY AUTO_INCREMENT,
    uom_name VARCHAR(45) NOT NULL
);

-- Create the products table
CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    uom_id INT NOT NULL,
    price_per_unit DOUBLE NOT NULL,
    FOREIGN KEY (uom_id) REFERENCES uom(uom_id)
);

-- Create the orders table
CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    total DOUBLE NOT NULL,
    datetime DATETIME NOT NULL
);

-- Create the order_details table
CREATE TABLE order_details (
    order_id INT NOT NULL,
    product_id INT NOT NULL,
    quantity DOUBLE NOT NULL,
    total_price DOUBLE NOT NULL,
    PRIMARY KEY (order_id, product_id),
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
);