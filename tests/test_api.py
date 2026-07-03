from app import app


def test_get_inventory():

    client = app.test_client()

    response = client.get("/inventory")

    assert response.status_code == 200


def test_get_single_item():

    client = app.test_client()

    response = client.get("/inventory/1")

    assert response.status_code == 200


def test_add_item():

    client = app.test_client()

    response = client.post(
        "/inventory",
        json={
            "barcode": "111",
            "product_name": "Milk",
            "brand": "Test",
            "price": 5,
            "stock": 10
        }
    )

    assert response.status_code == 201


def test_patch_item():

    client = app.test_client()

    response = client.patch(
        "/inventory/1",
        json={"stock": 99}
    )

    assert response.status_code == 200


def test_delete_item():

    client = app.test_client()

    response = client.delete(
        "/inventory/1"
    )

    assert response.status_code == 200