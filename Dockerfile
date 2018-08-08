FROM python:latest

ENV FLASK_APP=main.py

ENV FLASK_DEBUG=1

COPY ./app /app

WORKDIR /app

EXPOSE 8080

RUN pip install -r requirements.txt

ENTRYPOINT ["flask","run","--host=0.0.0.0","--port=8080"]