FROM ubuntu:latest
MAINTAINER Sam Landuydt "sam.landuydt@gmail.com"

RUN apt-get -y update
RUN apt-get install -y python-pip python-dev build-essential

ENV APP_ENTRYPOINT web
ENV LOG_LEVEL info
ENV MU_SPARQL_ENDPOINT 'http://database:8890/sparql'
ENV MU_SPARQL_UPDATEPOINT 'http://database:8890/sparql'
ENV MU_APPLICATION_GRAPH 'http://mu.semte.ch/application'

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ADD . /usr/src/app

ONBUILD RUN touch /usr/src/app/ext/__init__.py
ONBUILD RUN touch /usr/src/app/__init__.py

RUN ln -s /app /usr/src/app/ext \
     && cd /usr/src/app \
     && pip install -r requirements.txt

ONBUILD ADD . /app/
ONBUILD RUN cd /usr/src/app \
    && pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["touch" "touch /usr/src/app/ext/app/__init__.py"]
CMD ["web.py"]