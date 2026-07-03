import requests


def get_product(barcode):

    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"

    try:
        response = requests.get(url, timeout=10)

        if response.status_code != 200:
            return None

        try:
            data = response.json()
        except Exception:
            return None

        if data.get("status") == 1:

            product = data.get("product", {})

            return {
                "product_name":
                    product.get("product_name", ""),

                "brand":
                    product.get("brands", ""),

                "ingredients":
                    product.get(
                        "ingredients_text",
                        ""
                    )
            }

    except Exception as e:
        print(e)

    return None