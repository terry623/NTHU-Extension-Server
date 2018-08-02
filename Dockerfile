FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV STATIC_INDEX 1

COPY ./app /app

EXPOSE 80

WORKDIR /app

RUN pip install -r requirements.txt

RUN apt-get update
RUN apt-get install -y --no-install-recommends apt-utils
RUN apt-get install sudo

RUN apt-get install -y openjdk-8-jdk-headless net-tools wget
RUN wget --no-check-certificate https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-6.3.1.deb
RUN dpkg -i elasticsearch-6.3.1.deb