# syntax=docker/dockerfile:1

FROM python:3.9

# primarily theoretical: should work if the image gets built
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY app.py app.py

EXPOSE 5000

ENTRYPOINT flask run
