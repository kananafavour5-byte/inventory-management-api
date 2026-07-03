# Inventory Management System API

## Project Overview

This project is a Flask-based REST API for managing inventory items in a retail company. The application supports CRUD operations, external API integration using OpenFoodFacts, a command-line interface (CLI), and unit testing using pytest.

## Features

* View all inventory items
* View a single inventory item
* Add new inventory items
* Update inventory items
* Delete inventory items
* Search product information using OpenFoodFacts API
* Command-line interface (CLI)
* Unit testing with pytest
* Git version control with branches

## Technologies Used

* Python
* Flask
* Requests
* Pytest
* Git
* OpenFoodFacts API

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd inventory-management-api
```

Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running the Flask API

```bash
python app.py
```

The API runs on:

```
http://127.0.0.1:5000
```

## API Endpoints

### GET all inventory items

```
GET /inventory
```

### GET a single inventory item

```
GET /inventory/<id>
```

### Add a new inventory item

```
POST /inventory
```

### Update an inventory item

```
PATCH /inventory/<id>
```

### Delete an inventory item

```
DELETE /inventory/<id>
```

### Search OpenFoodFacts

```
GET /food/<barcode>
```

## Running the CLI

```bash
python cli.py
```

CLI options:

1. View Inventory
2. Add Product
3. Search OpenFoodFacts
4. Exit

## Running Tests

```bash
python -m pytest -v
```

## Notes

This project uses an in-memory Python list to simulate a database. Data resets whenever the Flask application restarts.
