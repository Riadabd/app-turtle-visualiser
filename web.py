import flask
import os
import helpers
from importlib import import_module
import builtins
from escape_helpers import sparql_escape
from rdflib.namespace import Namespace

# WSGI variable name used by the server
app = flask.Flask(__name__)

####################
## Example method ##
####################

@app.route('/templateExample/')
def query():
    """Example query: Returns all the triples in the application graph in a JSON
    format."""
    q =  " SELECT *"
    q += " WHERE{"
    q += "   GRAPH <http://mu.semte.ch/application> {"
    q += "     ?s ?p ?o"
    q += "   }"
    q += " }"
    return flask.jsonify(helpers.query(q))

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

#######################
## Start Application ##
#######################
if __name__ == '__main__':
    debug = True if (os.environ.get('MODE') == "development") else False
    app.run(debug=debug, host='0.0.0.0', port=80)
