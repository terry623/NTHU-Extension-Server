FROM python:latest

ENV FLASK_APP=main.py

ENV FLASK_DEBUG=1

COPY ./app /app

WORKDIR /app

EXPOSE 8080

RUN pip install -r requirements.txt

ENTRYPOINT ["flask","run","--host=0.0.0.0","--port=8080"]

RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install sudo

RUN apt-get install -y openjdk-8-jdk-headless net-tools wget
RUN wget --no-check-certificate https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.3.1.deb
RUN dpkg -i elasticsearch-6.3.1.deb