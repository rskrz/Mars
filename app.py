from flask import Flask, jsonify
from flask_cors import CORS
from solar import image_out

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/fetch', methods=['GET'])
def gen():
    image_out('mars.png')
    return jsonify('200')
