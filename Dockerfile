FROM ubuntu:latest
MAINTAINER Sam Landuydt "sam.landuydt@gmail.com"

RUN apt-get -y update
RUN apt-get install -y python-pip python-dev build-essential

ENV MU_SPARQL_ENDPOINT 'http://database:8890/sparql'
ENV MU_SPARQL_UPDATEPOINT 'http://database:8890/sparql'
ENV MU_APPLICATION_GRAPH 'http://mu.semte.ch/application'

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["web.py"]
