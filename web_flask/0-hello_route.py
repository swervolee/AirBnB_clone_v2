from flask import Flask


app = Flask(__name__)

"""Define a route for the root URL"""


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


"""Run the Flask application"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
