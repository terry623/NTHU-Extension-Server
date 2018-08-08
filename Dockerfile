FROM python:latest

ENV FLASK_APP=main.py

ENV FLASK_DEBUG=1

COPY ./app /app

EXPOSE 80

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["flask","run","--port=80"]