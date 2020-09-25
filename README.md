# Mu Python template

Template for [mu.semte.ch](http://mu.semte.ch)-microservices written in Python3. Based on the [Flask](https://palletsprojects.com/p/flask/)-framework.

## Quickstart

Create a `Dockerfile` which extends the `semtech/mu-python-template`-image and set a maintainer.
```docker
FROM semtech/mu-python-template
MAINTAINER Sam Landuydt <sam.landuydt@gmail.com>
```

Create a `web.py` entrypoint-file. (naming of the entrypoint can be configured through `APP_ENTRYPOINT`)
```python
@app.route("/hello")
def hello():
    return "Hello from the mu-python-template!"
```

Build the Docker-image for your service
```sh
docker build -t my-python-service .
```

Run your service
```sh
docker run -p 8080:80
```

You now should be able to access your service's endpoint
```sh
curl localhost:8080/hello
```

## Dependencies

If your service needs external libraries other than the ones already provided by the template (Flask, SPARQLWrapper and rdflib), you can specify those in a [`requirements.txt`](https://pip.pypa.io/en/stable/reference/pip_install/#requirements-file-format)-file. The template will take care of installing them when you build your Docker image.


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
               -p 80:80
               -d semtech/mu-python-template

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

### sparql_escape ; sparql_escape_{string|uri|date|datetime|time|bool|int|float}(value)
This method can be used to avoid SPARQL injection by escaping user input while constructing a SPARQL query.
The method checks the type of the given variable and returns the correct object string format,
depending on the type of the object. Current supported variables are: `datetime.time`, `datetime.date`, `str`, `int`, `float` and `boolean`.
For example:

    query =  " INSERT DATA {"
    query += "   GRAPH <http://mu.semte.ch/application> {"
    query += "     < %s > a <foaf:Person> ;" % user_uri
    query += "                   <foaf:name> %s ;" % sparql_escape(name)
    query += "                   <dc:created> %s ." % sparql_escape(date)
    query += "   }"
    query += " }"
    
Next to the `sparql_escape`, the template also provides a helper function per datatype that takes any value as parameter. E.g. `sparql_escape_uri("http://mu.semte.ch/application")`.

Next to the `sparql_escape`, the template also provides a helper function per datatype that takes any value as parameter. E.g. `sparql_escape_uri("http://mu.semte.ch/application")`.

## Example
There is one example method in the template: `GET /templateExample`. This method returns all triples in the triplestore from the SPARQL endpoint (beware for big databases!).
