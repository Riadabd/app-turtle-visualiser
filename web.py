import flask
import os
import sys
import helpers
import __builtin__
from rdflib.namespace import Namespace
import json

app = flask.Flask(__name__)

#########################
## Example methods ##
#########################

@app.route('/')
def hello_world():
    return 'Hello world'


@app.route('/example')
def query():
    """Example query: Returns all the triples in the application graph in a JSON
    format."""
    q =  " SELECT *"
    q += " WHERE{"
    q += "   GRAPH <http://mu.semte.ch/application> {"
    q += "     ?s ?p ?o"
    q += "   }"
    q += " }"
    return json.dumps(helpers.query(q))


##################
## Vocabularies ##
##################
mu = Namespace('http://mu.semte.ch/vocabularies/')
mu_core = Namespace('http://mu.semte.ch/vocabularies/core/')
mu_ext = Namespace('http://mu.semte.ch/vocabularies/ext/')

graph = os.environ.get('MU_APPLICATION_GRAPH')
SERVICE_RESOURCE_BASE = 'http://mu.semte.ch/services/'


#######################
## Start Application ##
#######################
if __name__ == '__main__':
    __builtin__.app = app
    __builtin__.helpers = helpers
    app_file = os.environ.get('APP_ENTRYPOINT')
    sys.path.append('/ext')
    __import__("%s" % app_file)

    debug = True if (os.environ.get('MODE') is 'development') else False
    app.run(debug=debug, host='0.0.0.0')
