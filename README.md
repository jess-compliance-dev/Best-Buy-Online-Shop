# 🛒 Best-Buy Online Shop

## Table of Contents
* Overview
* Technologies
* Features
* Setup
* Usage
* Project Purpose
* Future Improvements


## Overview

🛒 Best-Buy Online Shop is a console-based Python application simulating a real-world store.

Users can:
* Browse all available products
* Check total inventory quantity
* Place orders with multiple products
* Automatically calculate total payment
* Handle out-of-stock and input errors safely
* The project showcases object-oriented programming (OOP), modular design, and inventory management logic suitable for real-world applications.

## Technologies
* Python 3.x
* Object-Oriented Programming (Classes & Objects)
* Console-based user interface with colored output
* Standard Python libraries only

## Features
* Product listing with name, price, and quantity
* Inventory management and stock tracking
* Order processing with automatic total price calculation
* Product activation/deactivation based on stock
* Input validation and error handling
* Colored CLI output for better user feedback

## Setup

Clone the repository:
```bash
$ git clone https://github.com/yourusername/best-buy-online-shop.git
$ cd best-buy-online-shop
```

Verify Python is installed:
```bash
$ python --version
````

Run the application:
```bash
$ python main.py
````

🎯 How to Use

Start the program by running main.py.
Choose an option from the menu:

1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit

Select products by number and enter quantity.
Complete your order and view the total price.
Product quantities are automatically updated, and out-of-stock items are deactivated.

## Project Purpose

This project was built to:
* Practice Python OOP concepts (classes, methods, encapsulation)
* Implement inventory and order management logic
* Learn CLI design with user interaction
* Demonstrate exception handling and input validation
* Showcase clean, maintainable Python code for portfolios

## Future Improvements
* Implement a shopping cart class
* Add persistent storage (JSON / database)
* Web interface with Flask or Django
* User accounts and authentication
* Order history and reporting
* Unit testing with pytest
