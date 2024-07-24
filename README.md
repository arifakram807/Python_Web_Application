Grocery Store Management System (GSMS)
Overview
The Grocery Store Management System (GSMS) is a web application designed to streamline the management of grocery store operations, including inventory management, order processing, and product management. This project aims to provide a user-friendly interface for store managers to efficiently handle daily tasks.

Features
Product Management:

Add, update, and delete products.
View product details, including name, unit, and price per unit.
Order Management:

Create new orders with customer details.
Add multiple products to an order with dynamic pricing.
View and manage existing orders.
Unit of Measurement (UOM) Management:

View available units of measurement for products.
Technologies Used
Backend:

Flask: A lightweight WSGI web application framework in Python.
MySQL: A relational database management system to store application data.
SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library for Python.
Frontend:

HTML5: For structuring web content.
CSS3: For styling the web application.
Bootstrap: For responsive design and styling.
JavaScript & jQuery: For dynamic and interactive web elements.
Project Structure
Backend:

app.py: The main Flask application file containing route definitions and request handling.
sqlconnection.py: Handles the connection to the MySQL database.
products_dao.py: Data Access Object for managing product-related database operations.
uom_dao.py: Data Access Object for managing unit of measurement database operations.
Frontend:

index.html: Dashboard and main interface of the application.
manage-product.html: Interface for managing products.
order.html: Interface for creating and managing orders.
css/: Contains the CSS files for styling the web application.
js/: Contains JavaScript files for dynamic behavior and AJAX calls.

Usage
Dashboard: View and navigate between different sections of the application.
Manage Products: Add new products, update existing ones, and delete products.
New Order: Create new orders by adding products and specifying quantities.
