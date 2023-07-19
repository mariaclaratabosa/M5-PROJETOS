from menu import products


def calculate_tab(items):
    prices = []
    for item in items:
        for product in products:
            if (item["_id"] == product["_id"]):
                prices.append(product["price"] * item["amount"])
    subtotal = sum(prices)
    return {"subtotal": f"${round(subtotal, 2)}"}
