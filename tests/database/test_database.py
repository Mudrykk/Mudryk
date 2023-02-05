import pytest


@pytest.mark.database
def test_database_connection(database_api):
    database_api.test_connection()


@pytest.mark.database
def test_check_all_users(database_api):
    users = database_api.get_all_users()
    print(users)


@pytest.mark.database
def test_check_user_yurii(database_api):
    user = database_api.get_user_address_by_name("Sergii")

    assert user[0][0] == "Maydan Nezalezhnosti 1"
    assert user[0][1] == "Kyiv"
    assert user[0][2] == "3127"
    assert user[0][3] == "Ukraine"


@pytest.mark.database
def test_product_qnt_update(database_api):
    database_api.update_product_qnt_by_id(1, 25)
    p = database_api.select_product_by_id(1)

    assert p[0][0] == 25


@pytest.mark.database
def test_product_insert(database_api):
    database_api.insert_product(4, "печиво", "солодке", 30)
    p = database_api.select_product_by_id(4)

    assert p[0][0] == 30


@pytest.mark.database
def test_delete_product(database_api):
    database_api.insert_product(99, "test", "data", 999)
    database_api.delete_product_by_id(99)
    r = database_api.select_product_by_id(99)

    assert len(r) == 0


@pytest.mark.database
def test_detailed_orders(database_api):
    orders = database_api.get_detailed_orders()
    print(f"The orders are: {orders}")

    assert len(orders) == 1
    assert orders[0][0] == 1
    assert orders[0][1] == "Sergii"
    assert orders[0][2] == "солодка вода"
    assert orders[0][3] == "з цукром"
