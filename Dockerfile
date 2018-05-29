FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV STATIC_INDEX 1

COPY ./app /app

WORKDIR /app/app

RUN pip install -r requirements.txt