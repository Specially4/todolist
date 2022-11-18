FROM python:3.10-slim

WORKDIR app/
RUN sudo apt-get install libpq-dev python3-dev /bin/bash
RUN pip install poetry
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry install
COPY . .
CMD python manage.py runserver 0.0.0.0:8000
