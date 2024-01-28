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


@app.route('/states/<id>')
@app.route('/states')
def cities_by_states(id=None):
    """
    Displays an HTML page with a list of all State objects in DBStorage
    and its cities.States are sorted by name.
    """
    found = False
    state = storage.all(State)

    if id:
        for st in state.values():
            for city in st.cities:
                if city.id == id:
                    return render_template("9-states.html", state=state.values())
    if id:
        return render_template("9-states.html")
    return render_template("9-states.html", state=state)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)
