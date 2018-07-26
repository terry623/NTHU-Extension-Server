FROM tiangolo/uwsgi-nginx-flask:python3.6

ENV STATIC_INDEX 1

COPY ./app /app

EXPOSE 80

WORKDIR /app

RUN pip install -r requirements.txt