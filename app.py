from flask import Flask, jsonify
from flask_cors import CORS
from dotenv import load_dotenv
import os

# Load environment variables from a .env file
load_dotenv()

# Get the port from environment variable or default to 3030
port = int(os.getenv("PORT", 3030))

# Create the Flask app
app = Flask(__name__)

# Enable CORS for all routes and allow only GET methods
CORS(app, resources={r"/*": {"origins": "*"}}, methods=["GET"])

# Define the /products route
@app.route("/products", methods=["GET"])
def get_products():
    products = [
        {"id": 1, "name": "Dog Food", "price": 19.99},
        {"id": 2, "name": "Cat Food", "price": 34.99},
        {"id": 3, "name": "Bird Seeds", "price": 10.99},
    ]
    return jsonify(products)

# Start the server
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=port)
