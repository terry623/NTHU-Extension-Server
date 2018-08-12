FROM python:latest

ENV FLASK_APP=main.py
ENV FLASK_DEBUG=1
# ENV MONGO_ROLE_ACCOUNT=
# ENV MONGO_ROLE_PASSWORD=

COPY ./app /app
WORKDIR /app

EXPOSE 8080

RUN pip install -r requirements.txt
ENTRYPOINT ["flask","run","--host=0.0.0.0","--port=8080"]

RUN apt-get update
RUN apt-get install -y --allow-unauthenticated sudo

RUN apt-get install -y --allow-unauthenticated openjdk-8-jdk-headless wget
RUN wget --no-check-certificate https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.3.1.deb
RUN dpkg -i elasticsearch-6.3.1.deb