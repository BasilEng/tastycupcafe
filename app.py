from flask import Flask, request, jsonify

app = Flask(__name__)

ticket_counter = 1
orders = []

@app.route('/')
def home():
    return "Order system is running."

@app.route('/order', methods=['POST'])
def take_order():
    global ticket_counter
    data = request.get_json()
    order = {
        'ticket': ticket_counter,
        'items': data.get('items', [])
    }
    orders.append(order)
    ticket_counter += 1
    return jsonify(order), 200

if __name__ == '__main__':
    app.run()
