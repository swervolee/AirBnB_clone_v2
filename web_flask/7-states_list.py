#!/usr/bin/python3
"""

Starts a Flask web application.

"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close(cmd):
    storage.close()


@app.route("/states_list")
def state_list():
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
