#!/usr/bin/python3
"""
Starts a Flask web application.
The application listens on 0.0.0.0, port 5000.
Routes:
/states_list: HTML page with a list of all State objects in DBStorage.
"""
from flask import Flask, render_template, abort
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_db(exc):
    """close the current session of sqlalchemist"""
    storage.close()


@app.route("/states")
def states():
    """Displays an HTML page with a list of all States.

    States are sorted by name.
    """
    states = storage.all(State)
    return render_template("9-states.html", state=states)


@app.route("/states/<id>")
def states_id(id):
    """Displays an HTML page with info about <id>, if it exists."""
    for state in storage.all(State).values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
