import flask
import os
import helpers
from SPARQLWrapper import SPARQLWrapper, JSON

app = flask.Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world'

sparqlQuery = SPARQLWrapper(os.environ.get('MU_SPARQL_ENDPOINT'), returnFormat=JSON)
sparqlUpdate = SPARQLWrapper(os.environ.get('MU_SPARQL_UPDATEPOINT'), returnFormat=JSON)

##################
## Vocabularies ##
##################
import rdflib.namespace as ns
mu = ns.Namespace('http://mu.semte.ch/vocabularies/')
mu_core = ns.Namespace('http://mu.semte.ch/vocabularies/core/')
mu_ext = ns.Namespace('http://mu.semte.ch/vocabularies/ext/')

graph = os.environ.get('MU_APPLICATION_GRAPH')
SERVICE_RESOURCE_BASE = 'http://mu.semte.ch/services/'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
