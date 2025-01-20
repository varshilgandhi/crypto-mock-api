from flask import Flask, jsonify, request
from flask_restx import Api, Resource
from data.crypto_data import crypto_prices

app = Flask(__name__)
api = Api(app, title="Crypto Mock API", description="API for simulating cryptocurrency operations")

@api.route('/')
class Home(Resource):
    def get(self):
        """Welcome Message"""
        return jsonify({"message": "Welcome to the Crypto Mock API!"})

@api.route('/getCryptoPrices')
class GetCryptoPrices(Resource):
    def get(self):
        """Fetch current crypto prices"""
        return jsonify({"crypto_prices": crypto_prices})

@api.route('/executeTrade')
class ExecuteTrade(Resource):
    def post(self):
        """Simulate a cryptocurrency trade"""
        data = request.get_json()
        symbol = data.get('symbol')
        quantity = data.get('quantity')
        price = data.get('price')

        if not symbol or not quantity or not price:
            return {"error": "Missing required parameters: symbol, quantity, or price"}, 400

        # Validate symbol
        crypto = next((item for item in crypto_prices if item["symbol"] == symbol), None)
        if not crypto:
            return {"error": f"Cryptocurrency with symbol '{symbol}' not found"}, 404

        # Simulate trade
        trade_type = "buy" if quantity > 0 else "sell"
        total_cost = abs(quantity) * price

        return {
            "message": f"Successfully executed {trade_type} trade",
            "trade_details": {
                "symbol": symbol,
                "trade_type": trade_type,
                "quantity": quantity,
                "price": price,
                "total_cost": total_cost
            }
        }

if __name__ == '__main__':
    app.run(debug=True)
