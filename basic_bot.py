import logging
from binance import Client
from binance.exceptions import BinanceAPIException

class BasicBot:
    def __init__(self, api_key, api_secret, testnet=True):
        self.client = Client(api_key, api_secret)

        if testnet:
            self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

        logging.info("Binance Futures Testnet client initialized")

    def place_market_order(self, symbol, side, quantity):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )
            logging.info(f"Market order placed: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Market order error: {e}")
            raise

    def place_limit_order(self, symbol, side, quantity, price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )
            logging.info(f"Limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Limit order error: {e}")
            raise

    def place_stop_limit_order(self, symbol, side, quantity, price, stop_price):
        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="STOP",
                quantity=quantity,
                price=price,
                stopPrice=stop_price,
                timeInForce="GTC"
            )
            logging.info(f"Stop-limit order placed: {order}")
            return order
        except BinanceAPIException as e:
            logging.error(f"Stop-limit order error: {e}")
            raise
