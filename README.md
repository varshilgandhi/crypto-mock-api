
# Crypto Mock API

API for simulating cryptocurrency operations, including fetching prices and executing trades with Swagger documentation.

## Features
- **Fetch Current Prices**: Retrieve mock cryptocurrency prices using a GET request.
- **Simulate Trades**: Execute buy or sell trades by providing symbol, quantity, and price.
- **Swagger Documentation**: View and interact with the API directly through an auto-generated Swagger UI.

## Technologies Used
- **Flask**: Backend framework for the API.
- **Flask-RESTX**: For Swagger documentation.
- **Python**: Programming language.

## Endpoints

### 1. Welcome Message
- **URL**: `/`
- **Method**: `GET`
- **Description**: Returns a welcome message.

---

### 2. Fetch Crypto Prices
- **URL**: `/getCryptoPrices`
- **Method**: `GET`
- **Description**: Fetches mock cryptocurrency prices.
- **Response**:
  ```json
  {
    "crypto_prices": [
      { "name": "Bitcoin", "price": 43780.5, "symbol": "BTC" },
      { "name": "Ethereum", "price": 3200.8, "symbol": "ETH" },
      { "name": "Binance Coin", "price": 420.1, "symbol": "BNB" }
    ]
  }
  ```

---

### 3. Execute a Trade
- **URL**: `/executeTrade`
- **Method**: `POST`
- **Description**: Simulates a buy or sell trade.
- **Request Body**:
  ```json
  {
    "symbol": "BTC",
    "quantity": 0.5,
    "price": 44000
  }
  ```
- **Response**:
  ```json
  {
    "message": "Successfully executed buy trade",
    "trade_details": {
      "symbol": "BTC",
      "trade_type": "buy",
      "quantity": 0.5,
      "price": 44000,
      "total_cost": 22000
    }
  }
  ```

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/varshilgandhi/crypto-mock-api.git
   ```
2. Navigate to the project directory:
   ```bash
   cd crypto-mock-api
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python app.py
   ```
5. Open the application in a browser:
   - Swagger UI: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Project Structure

```
crypto-mock-api/
├── app.py              # Main application file
├── requirements.txt    # Dependencies
├── data/
│   └── crypto_data.py  # Mock crypto data
├── docs/               # Documentation
└── tests/              # Test scripts (future use)
```

---

## Future Enhancements
- Add user authentication for executing trades.
- Connect the API to live cryptocurrency price feeds.
- Include more trade-related features (e.g., order history, transaction logs).

---

## License
This project is licensed under the MIT License.
