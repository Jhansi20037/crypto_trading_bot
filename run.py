import logging
from bot.basic_bot import BasicBot
from bot.cli import run_cli

logging.basicConfig(
    filename="logs/bot.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

API_KEY = "API_KEY_12345"
API_SECRET = "API_SECRET_12345"

bot = BasicBot(API_KEY, API_SECRET, testnet=True)
run_cli(bot)
