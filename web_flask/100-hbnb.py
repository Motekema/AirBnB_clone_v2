#!/usr/bin/python3
"""
Flask application for displaying HBNB filters
"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from sqlalchemy.orm import joinedload

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """
    Display an HTML page (similar to 8-index.html from the web_static project)
    with information about states, cities, amenities, and places
    """
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()

    return render_template('100-hbnb.html', states=states, cities=cities,
                           amenities=amenities, places=places)


@app.teardown_appcontext
def close_storage(exception):
    """
    Closes the storage connection on application context teardown
    """
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
