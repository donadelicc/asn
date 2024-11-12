from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/order/<product>')
def order(product):
    return render_template('order.html', product=product)

if __name__ == '__main__':
    app.run(debug=True)
