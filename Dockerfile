FROM python:3.10-slim-buster

RUN apt-get update --fix-missing
# RUN apt-get upgrade -y

RUN python -m pip install --upgrade pip

RUN apt-get install build-essential -y

RUN apt-get install -y supervisor nano

ENV INSTALL_PATH /the_onahs

RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .
ADD supervisord.conf /etc/supervisord.conf

ENTRYPOINT ["supervisord", "--nodaemon", "--configuration", "/etc/supervisord.conf"]
