# Mu Python template

Template for running Python microservices

## Using the template

1) Extend the `samldd/mu-python-template` and set a maintainer.

2) Configure your entrypoint through the environment variable `APP_ENTRYPOINT` (default: `web.py`).

Use the web.py template as a start point for developing your application. Remove the default methods en implement your own.

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
