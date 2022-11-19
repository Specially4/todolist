FROM python:3.10-slim

ENV PYTHONBUFFERED 1

WORKDIR todolist/
RUN pip install poetry
COPY poetry.lock .
COPY pyproject.toml .
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev --no-ansi --no-root
COPY . .
CMD python manage.py runserver 0.0.0.0:8000
