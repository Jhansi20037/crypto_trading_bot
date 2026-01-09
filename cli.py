import argparse
from bot.validator import validate_order

def run_cli(bot):
    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")

    parser.add_argument("--symbol", required=True, help="Trading pair e.g. BTCUSDT")
    parser.add_argument("--side", required=True, choices=["BUY", "SELL"])
    parser.add_argument("--type", required=True, choices=["MARKET", "LIMIT", "STOP_LIMIT"])
    parser.add_argument("--quantity", required=True, type=float)
    parser.add_argument("--price", type=float)
    parser.add_argument("--stop_price", type=float)

    args = parser.parse_args()

    validate_order(
        args.symbol,
        args.side,
        args.type,
        args.quantity,
        args.price,
        args.stop_price
    )

    if args.type == "MARKET":
        return bot.place_market_order(args.symbol, args.side, args.quantity)

    if args.type == "LIMIT":
        return bot.place_limit_order(args.symbol, args.side, args.quantity, args.price)

    if args.type == "STOP_LIMIT":
        return bot.place_stop_limit_order(
            args.symbol,
            args.side,
            args.quantity,
            args.price,
            args.stop_price
        )
