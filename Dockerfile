FROM ubuntu:14.04
MAINTAINER Svetlana Galkina <galkina.s.a@gmail.com>
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get -qq update
RUN apt-get -qq install python-pip python-requests python-dev python-virtualenv
ADD todo_api/ /todo_api/
RUN mkdir -p /venv/
RUN virtualenv -p python3 /venv/
RUN /venv/bin/pip install -r todo_api/requirements.txt
EXPOSE 5000
CMD cd /todo_api/ && /venv/bin/python server.py