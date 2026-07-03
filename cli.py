import requests

BASE_URL = "http://127.0.0.1:5000"


def view_inventory():
    response = requests.get(f"{BASE_URL}/inventory")
    print(response.json())


def add_product():
    product = {
        "barcode": input("Barcode: "),
        "product_name": input("Product Name: "),
        "brand": input("Brand: "),
        "price": float(input("Price: ")),
        "stock": int(input("Stock: "))
    }

    response = requests.post(
        f"{BASE_URL}/inventory",
        json=product
    )

    print(response.json())


def search_api():
    barcode = input("Enter barcode: ")

    response = requests.get(
        f"{BASE_URL}/food/{barcode}"
    )

    print(response.json())


while True:

    print("\nInventory System")
    print("1. View Inventory")
    print("2. Add Product")
    print("3. Search OpenFoodFacts")
    print("4. Exit")

    choice = input("> ")

    if choice == "1":
        view_inventory()

    elif choice == "2":
        add_product()

    elif choice == "3":
        search_api()

    elif choice == "4":
        break