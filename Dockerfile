FROM python:2.7.10

RUN apt-get -y update && apt-get -y install git && \
    pip install psycopg2 && \
    pip install flask && \
    pip install Flask-SQLAlchemy && \
    git clone https://github.com/stefanteixeira/todoapp-flask.git

ADD ./start.sh /

EXPOSE 5000

ENTRYPOINT ./start.sh
