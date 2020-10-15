from flask import Flask
app = Flask(__name__)

#Larissa
@app.route('/customers')
def get_all_customers():
    return 'Hello, World!'

#Larissa
@app.route('/cars')
def get_all_cars():
    return 'Hello, World!'


@app.route('/customer/<id>/book/<car_id>', methods=["POST"])
def book_car(id, car_id):
    return 'Hello, World!'

@app.route('/customer/<id>/history')
def get_history(id):
    return 'Hello, World!'

if __name__ == '__main__':
    # Start webserver
    for i in range(100):
        try:
            app.run(host="0.0.0.0", port=8080 + i, debug=True)
            break
        except OSError:
            pass
