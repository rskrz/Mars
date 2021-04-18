from flask import Flask, jsonify
from flask_cors import CORS
from solar import image_out

# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)
app.config['CORS_ORIGINS'] = ["localhost"]
app.config['CORS_HEADERS'] = ["Access-Control-Allow_origin"]

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

# sanity check route
@app.route('/fetch', methods=['GET'])
def gen():
    image_out('mars.png')
    response = jsonify('200')
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

if __name__ == '__main__':
    app.run()