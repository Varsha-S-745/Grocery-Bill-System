# Grocery-Bill-System
This Grocery Billing System is built using Python Flask and MySQL, providing a RESTful API to manage products, units of measurement (UOM), and customer orders. It supports fetching product and UOM details, inserting/deleting products, and handling orders.

Objective:
The objective of this project is to develop a backend system for managing the core operations of a grocery store, such as handling product listings, units of measurement (UOM), and customer orders. By creating a RESTful API using Flask and MySQL, the system enables efficient product management, order processing, and smooth integration with frontend interfaces. The goal is to simplify store management through a reliable and scalable software solution.

Installation Required Packages:
Python 3.x
Flask
mysql-connector-python

Database Setup in Mysql:
Create a MySQL database named grocery.
Create necessary tables for products, orders, and uoms.
Provide appropriate privileges to the MySQL user.

Running the Application:
Start the MySQL server.
Run the Flask server using python app.py.
API will be available at http://localhost:5000.

Code Development Idea:
The application is modular, separating database logic into DAO (Data Access Object) files:
products.py handles all product-related queries.
orders.py manages order transactions.
uom.py provides units of measurement.
The app.py file serves as the main entry point and defines Flask routes for:
Fetching products and UOMs.
Inserting or deleting products.
Creating and retrieving orders.
All requests and responses are in JSON format. Cross-Origin Resource Sharing (CORS) is enabled to allow frontend clients to interact with the API without restrictions.

Applications and Tools Used:
Backend Framework: Flask (Python)
Database: MySQL
Database Connector: mysql-connector-python
API Design: RESTful API using Flask routes
Development Tools:
Code Editor: VS Code / PyCharm
MySQL Workbench / phpMyAdmin for DB management
Postman or cURL for testing API endpoints
Version Control: Git (optional)



