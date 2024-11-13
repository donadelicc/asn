from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from util.upload_data import upload_to_blob_storage


app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order/<product>')
def order(product):
    return render_template('order.html', product=product)

@app.route('/api/waitlist', methods=['POST'])
def add_to_waitlist():
    try:
        # Get the data from the request
        data = request.get_json()
        if not data:
            return jsonify({"error": "No data received"}), 400
        
        print("Received data:", data)  # Debug print
        
        upload_to_blob_storage(data)
        
        return jsonify({"message": "Successfully added to waitlist"}), 200
        
    except Exception as e:
        print("Error:", str(e))  # Debug print
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
