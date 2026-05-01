from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Home route
@app.route('/')
def home():
    return jsonify(message="Bem-vindo ao My App FH Backend!")

# API route example
@app.route('/api/data', methods=['GET'])
def get_data():
    data = {
        "id": 1,
        "name": "My App FH",
        "version": "1.0.0",
        "status": "running"
    }
    return jsonify(data)

# API route to accept POST requests
@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()
    return jsonify({"message": "Data received", "data": data}), 201

# Error handler
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not found"}), 404

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)