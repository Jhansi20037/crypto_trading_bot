def validate_order(symbol, side, order_type, quantity, price=None, stop_price=None):
    if not symbol.endswith("USDT"):
        raise ValueError("Only USDT-M futures symbols are supported")

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL")

    if order_type not in ["MARKET", "LIMIT", "STOP_LIMIT"]:
        raise ValueError("Order type must be MARKET, LIMIT, or STOP_LIMIT")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero")

    if order_type == "LIMIT" and price is None:
        raise ValueError("Price is required for LIMIT orders")

    if order_type == "STOP_LIMIT":
        if price is None or stop_price is None:
            raise ValueError("Price and stop_price are required for STOP_LIMIT orders")
