from menu import products
from collections import Counter


def get_product_by_id(product_id):
    if type(product_id) != int:
        raise TypeError("product id must be an int")

    for product in products:
        if product["_id"] == product_id:
            return product
    return {}


def get_products_by_type(product_type):
    if type(product_type) != str:
        raise TypeError("product type must be a str")

    products_found = []
    for product in products:
        if product["type"] == product_type:
            products_found.append(product)
    return products_found


def add_product(menu, **kwargs):
    max_id = 0
    for product in menu:
        if product["_id"] > max_id:
            max_id = product["_id"]

    new_id = max_id + 1

    new_product = {"_id": new_id}
    new_product.update(kwargs)

    menu.append(new_product)

    return new_product


def menu_report():
    products_count = len(products)

    total_price = sum(product["price"] for product in products)
    average_price = round((total_price / products_count), 2)

    product_types = Counter(product["type"] for product in products)
    most_common_type = product_types.most_common(1)[0][0]

    return (
        f"Products Count: {products_count} - "
        f"Average Price: ${average_price} - "
        f"Most Common Type: {most_common_type}"
    )
