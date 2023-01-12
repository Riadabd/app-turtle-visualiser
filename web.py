import os
from importlib import import_module
import builtins

import flask
from flask import jsonify, request, Response
from rdflib.namespace import Namespace

import helpers
from escape_helpers import sparql_escape

from rdf import create_graph, read_graph_render

# WSGI variable name used by the server
app = flask.Flask(__name__)

##################
## Vocabularies ##
##################
mu = Namespace('http://mu.semte.ch/vocabularies/')
mu_core = Namespace('http://mu.semte.ch/vocabularies/core/')
mu_ext = Namespace('http://mu.semte.ch/vocabularies/ext/')

SERVICE_RESOURCE_BASE = 'http://mu.semte.ch/services/'

builtins.app = app
builtins.helpers = helpers
builtins.sparql_escape = sparql_escape

# Import the app from the service consuming the template
app_file = os.environ.get('APP_ENTRYPOINT')
try:
    module_path = 'ext.app.{}'.format(app_file)
    import_module(module_path)
except Exception as e:
    helpers.log(str(e))


@app.route('/hello')
def hello():
    return jsonify({"hello": "Hello from turtle-visualiser!"})


@app.route('/graph', methods=['POST'])
def graph():
    headers = {'Content-Type': 'image/svg'}
    turtle_input = request.data
    if (not turtle_input):
        return Response(headers=headers, status=204)
    else:
        create_graph(turtle_input)
        return Response(read_graph_render(), headers=headers)


#######################
## Start Application ##
#######################
if __name__ == '__main__':
    debug = os.environ.get('MODE') == "development"
    app.run(debug=debug, host='0.0.0.0', port=80)
