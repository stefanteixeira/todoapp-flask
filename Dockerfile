FROM python:2.7.10

ADD ./start.sh /
ADD ./requirements.txt /

RUN pip install -r requirements.txt && \
    git clone https://github.com/stefanteixeira/todoapp-flask.git

EXPOSE 5000

ENTRYPOINT ./start.sh
