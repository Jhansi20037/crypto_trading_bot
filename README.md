🚀 Crypto Trading Bot – Binance Futures Testnet (Python)

A simplified Python-based trading bot built using the official Binance Futures Testnet (USDT-M) API.
The project demonstrates clean API integration, command-line interaction, input validation, logging, and error handling for automated trade execution.

✨ Features

Binance USDT-M Futures Testnet integration
Place Market and Limit orders
Support for BUY and SELL order sides
Command-Line Interface (CLI) using argparse
Input validation for symbol, order type, quantity, and price
Centralized logging of API requests, responses, and errors
Modular and reusable Python code structure
Optional STOP-LIMIT order implementation (bonus)

🛠 Tech Stack

Python 3
python-binance
argparse
logging

📂 Project Structure
crypto_trading_bot/
│
├── bot/
│   ├── __init__.py
│   ├── basic_bot.py
│   ├── cli.py
│   └── validator.py
│
├── logs/
│   └── bot.log
│
├── requirements.txt
├── run.py
└── README.md


⚙️ Setup Instructions

Register and log in to Binance Futures Testnet
👉 https://testnet.binancefuture.com

Generate Futures Testnet API Key and Secret
Enable Futures permission
Disable IP restriction and withdrawal access
Install dependencies:
pip install -r requirements.txt
Add API credentials temporarily inside run.py for local testing:
API_KEY = "YOUR_TESTNET_API_KEY"
API_SECRET = "YOUR_TESTNET_API_SECRET"

Usage
Market Order
python3 run.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
Limit Order
python3 run.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 45000

Logging
All API interactions are logged to:
logs/bot.log

⚠️ Note on Binance Futures Testnet

While the trading bot fully implements market, limit, and stop-limit order logic using the official Binance Futures API, actual order execution on the Binance Futures Testnet may be restricted due to:
Testnet account permission limitations
Regional or KYC-based restrictions
Testnet API instability
Despite these constraints, all API requests, validations, and error handling are correctly implemented and logged.
This project focuses on robust system design, API integration, CLI usability, and fault-tolerant behavior rather than testnet reliability.

🔐 Security Notice

API keys are never committed to version control
Placeholder values are used in the repository
This project is strictly for educational and evaluation purposes

👩‍💻 Author

Jhansilaxmi
Junior Python Developer – Crypto Trading Bot Assignment

