from flask import Flask, jsonify, render_template, request
import json
import os
from datetime import datetime

app = Flask(__name__)

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
        
        time = datetime.now().isoformat()
        
        # Add timestamp to the entry
        data['timestamp'] = time
        
        # Load existing waitlist data
        waitlist_file = f'waitlist_{time}.json'
        if os.path.exists(waitlist_file):
            with open(waitlist_file, 'r') as f:
                waitlist = json.load(f)
        else:
            waitlist = []
        
        # Append new entry
        waitlist.append(data)
        
        # Save updated waitlist
        with open(waitlist_file, 'w') as f:
            json.dump(waitlist, f, indent=4)
        
        return jsonify({"message": "Successfully added to waitlist"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
