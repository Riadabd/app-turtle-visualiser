# Mu Python template

Template for running Python microservices

## Using the template

1) Extend the `samldd/mu-python-template` and set a maintainer.

2) Configure your entrypoint through the environment variable `APP_ENTRYPOINT` (default: `web.py`).

3) Write the python requirements in a requirements.txt file. (Flask, SPARQLWrapper and rdflib are standard installed)

Create the entry point file and add methods with URL's. 
The flask app is added to the python builtin and can be accessed by using the app variable, as shown in following example:

    @app.route(/exampleMethod)
    def exampleMethod():
        return example

## Example Dockerfile

    FROM samldd/mu-python-template:latest
    MAINTAINER Sam Landuydt <sam.landuydt@gmail.com>
    # ONBUILD of mu-python-template takes care of everything

## Configuration

The template supports the following environment variables:

- `MU_SPARQL_ENDPOINT` is used to configure the SPARQL endpoint.

  - By default this is set to `http://database:8890/sparql`. In that case the triple store used in the backend should be linked to the microservice container as `database`.


- `MU_APPLICATION_GRAPH` specifies the graph in the triple store the microservice will work in.

  - By default this is set to `http://mu.semte.ch/application`. The graph name can be used in the service via `settings.graph`.


- `MU_SPARQL_TIMEOUT` is used to configure the timeout (in seconds) for SPARQL queries.

## Develop a microservice using the template

To use the template while developing your app, start a container in development mode with your code folder on the host machine mounted in `/app`:

    docker run --volume /path/to/your/code:/app
               -e MODE=development
               -d python-template

Code changes will be automatically picked up by Flask.

## Helper methods
The template provides the user with several helper methods. Most helpers can be used by calling: "helpers.<helperName>", except the sparql_escape helper: "sparql_escape(var)".

### log(msg)

The template provides a log object to the user for logging. Just do log("Hello world").
The log level can be set through the LOG_LEVEL environment variable
 (default: info, values: debug, info, warning, error, critical).

Logs are written to the /logs directory in the docker container.

### generate_uuid()

Generate a random UUID (String).

### session_id_header(request)

Get the session id from the HTTP request headers.

### rewrite_url_header(request)

Get the rewrite URL from the HTTP request headers.

### validate_json_api_content_type(request)

Validate whether the Content-Type header contains the JSONAPI Content-Type. Returns a 400 otherwise.

### validate_resource_type(expected_type, data)

Validate whether the type specified in the JSON data is equal to the expected type. Returns a 409 otherwise.

### error(title, status = 400)

Returns a JSONAPI compliant error response with the given status code (default: 400).

### query(query)

Executes the given SPARQL select/ask/construct query.

### update(query)

Executes the given SPARQL update query.

### update_modified(subject, modified = datetime.now())

Executes a SPARQL query to update the modification date of the given subject URI (string).
The date defaults to now.

### sparql_escape(var)
This method can be used to avoid SPARQL injection by escaping user input while constructing a SPARQL query.
The method checks the type of the given variable and returns the correct object string format,
depending on the type of the object. Current supported variables are: datetime.time, datetime.date, str, int, float and boolean.
For example:

    query =  " INSERT DATA {"
    query += "   GRAPH <http://mu.semte.ch/application> {"
    query += "     < %s > a <#{RDF::Vocab::FOAF.Person}> ;" % user_uri
    query += "                   <#{RDF::Vocab::FOAF.name}> %s ;" % sparql_escape(name)
    query += "                   <#{RDF::Vocab::DC.created}> %s ." % sparql_escape(date)
    query += "   }"
    query += " }"

## Example
There is one example method in the template: "/templateExample/" this methods returns all trippels in the tripple store from the sparql endpoint (beware for big databases!).