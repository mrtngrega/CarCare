import datetime
from functools import wraps
from flask import Flask, jsonify, request
import jwt
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
SECRET_KEY = "carcare_detailing_tajny_klic_123"

# Simulácia databázy v pamäti
users_db = {}

services_db = [
    {
        "id": 1,
        "name": "Kompletné čistenie interiéru",
        "base_price": 100.0,
        "description": "Tepovanie, ošetrenie kože a plastov",
    },
    {
        "id": 2,
        "name": "Keramická ochrana laku",
        "base_price": 300.0,
        "description": "Viacstupňové leštenie + aplikácia keramiky",
    },
]

PRICE_MULTIPLIERS = {"small": 1.0, "medium": 1.2, "suv": 1.4}


@app.route("/")
def home():
    return jsonify({"message": "Vitajte na API CarCare Detailing!"})


@app.route("/api/services", methods=["GET"])
def get_services():
    vehicle_type = request.args.get("vehicle_type", "small").lower()
    multiplier = PRICE_MULTIPLIERS.get(vehicle_type, 1.0)

    calculated_services = []
    for service in services_db:
        calculated_services.append(
            {
                "id": service["id"],
                "name": service["name"],
                "description": service["description"],
                "calculated_price": round(service["base_price"] * multiplier, 2),
                "vehicle_type": vehicle_type,
            }
        )

    return jsonify(calculated_services)


if __name__ == "__main__":
    app.run(debug=True, port=5000)