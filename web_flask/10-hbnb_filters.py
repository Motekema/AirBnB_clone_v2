#!/usr/bin/python3
"""
Flask application for displaying HBNB filters
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)

@app.route('/hbnb_filters', strict_slashes=False)
def display_hbnb_filters():
    """
    Display an HTML page (similar to 6-index.html from the static folder)
    with information about states and amenities
    """
    states = storage.all("State").values()
    amenities = storage.all("Amenity").values()
    return render_template('10-hbnb_filters.html', states=states, amenities=amenities)

@app.teardown_appcontext
def close_storage(exception):
    """
    Closes the storage connection on application context teardown
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
