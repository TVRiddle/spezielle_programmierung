from flask import Flask
app = Flask(__name__)

@app.route('/<int:id>')
def hello_world(id):
    return 'Hello, World!'

if __name__ == '__main__':
    # Start webserver
    for i in range(100):
        try:
            app.run(host="0.0.0.0", port=8080 + i, debug=True)
            break
        except OSError:
            pass
