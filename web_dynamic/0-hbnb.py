#!/usr/bin/python3
""" Starts a Flash Web Application """
import uuid
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/0-hbnb/', strict_slashes=False)
def hello_hbnb():
    """ Renders 0-hbnb.html with a cache_id """
    cache_id = str(uuid.uuid4())
    return render_template('0-hbnb.html', cache_id=cache_id)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
