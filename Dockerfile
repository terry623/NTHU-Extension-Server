FROM python:3.6

COPY ./app /app

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT ["python","main.py"]

EXPOSE 8080