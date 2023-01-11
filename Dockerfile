FROM tiangolo/meinheld-gunicorn:python3.8
MAINTAINER Michaël Dierick "michael@dierick.io"

# Gunicorn Docker config
ENV MODULE_NAME web
ENV PYTHONPATH "/usr/src/app:/app"
ENV WEB_CONCURRENCY "1"

# Overrides the start.sh used in `tiangolo/meinheld-gunicorn`
COPY ./start.sh /start.sh
RUN chmod +x /start.sh


# Template config
ENV APP_ENTRYPOINT web
ENV LOG_LEVEL info
ENV MU_SPARQL_ENDPOINT 'http://database:8890/sparql'
ENV MU_SPARQL_UPDATEPOINT 'http://database:8890/sparql'
ENV MU_APPLICATION_GRAPH 'http://mu.semte.ch/application'

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app

RUN apt update
RUN apt install --no-install-recommends --assume-yes graphviz

RUN ln -s /app /usr/src/app/ext \
     && cd /usr/src/app \
     && pip3 install -r requirements.txt

ONBUILD ADD . /app/
ONBUILD RUN touch /app/__init__.py
ONBUILD RUN cd /app/ \
    && if [ -f requirements.txt ]; then pip install -r requirements.txt; fi


