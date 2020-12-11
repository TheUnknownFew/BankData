import json

from flask import Flask, send_from_directory, request

from python.cmpsc import pathing, model
from python.cmpsc.pathing import html_dir, template_dir

server = Flask(__name__)


@server.route('/', methods=['GET'])
def get_index():
    """
    :return: Returns the main site html.
    """
    return send_from_directory(html_dir, 'index.html', mimetype='text/html')


@server.route('/css/index.css', methods=['GET'])
def get_css():
    """
    :return: Returns the css for the main site html.
    """
    return send_from_directory(pathing.get(html_dir, 'css'), 'index.css', mimetype='text/css')


@server.route('/scripts/main.js', methods=['GET'])
def get_main_javascript():
    """
    :return: Returns the JavaScript used for the main html.
    """
    return send_from_directory(pathing.get(html_dir, 'scripts'), 'main.js', mimetype='text/javascript')


@server.route('/predict', methods=['POST'])
def prediction_endpoint():
    """
    :return: Returns a prediction result based off the data passed in by the request.
    """
    return json.dumps({"result": model.make_prediction(request.json)})


if __name__ == '__main__':
    server.run()
