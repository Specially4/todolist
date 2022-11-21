FROM python:3.10-slim

ENV PYTHONBUFFERED 1

WORKDIR todolist/
COPY requirements_unix.txt requirements.txt
COPY .env_docker .env
RUN pip install -r requirements.txt
COPY . .
CMD python manage.py runserver 0.0.0.0:8000
