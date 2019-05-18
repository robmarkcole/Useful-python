import api as api

TEST_CURRENCY = "GBP"
TEST_CONVERSION_RATE = 1.0

TEST_ORDER = {
    "order": {
        "id": 12345,
        "items": [
            {"product_id": 1, "quantity": 1},
            {"product_id": 2, "quantity": 5},
            {"product_id": 3, "quantity": 1},
        ],
    }
}

TEST_ORDER_FORMATTED = {1: 1, 2: 5, 3: 1}

TEST_VALID_GBP_ORDER = {
    1: {"quantity": 1, "total_price": 599.0, "total_VAT": 119.8},
    2: {"quantity": 5, "total_price": 1250.0, "total_VAT": 0.0},
    3: {"quantity": 1, "total_price": 250.0, "total_VAT": 0.0},
    "total_price": 2099.0,
    "total_VAT": 119.8,
    "currency": "GBP",
}


def test_format_pricing():
    assert api.format_pricing(api.raw_pricing)[1].price == 599


def test_format_order():
    assert api.format_order(TEST_ORDER) == TEST_ORDER_FORMATTED


def test_calc_order_details():
    assert (
        api.calc_order_details(
            api.format_order(TEST_ORDER),
            api.format_pricing(api.raw_pricing),
            TEST_CONVERSION_RATE,
            TEST_CURRENCY,
        )
        == TEST_VALID_GBP_ORDER
    )
