from flask import Flask, jsonify

app = Flask(__name__)

# Sample inventory endpoint for Pharmacy Management System
@app.route('/')
def home():
    return jsonify({
        "status": "success",
        "system": "Pharmacy Management System",
        "message": "Pharmacy API is running smoothly!"
    })

@app.route('/inventory')
def get_inventory():
    inventory = [
        {"id": 1, "name": "Paracetamol", "stock": 150, "price": 5.0},
        {"id": 2, "name": "Amoxicillin", "stock": 80, "price": 12.5},
        {"id": 3, "name": "Ibuprofen", "stock": 200, "price": 8.0}
    ]
    return jsonify(inventory)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)