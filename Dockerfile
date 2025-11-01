FROM python:3.13-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY pyproject.toml poetry.lock ./

RUN pip install --upgrade pip && pip install poetry && poetry config virtualenvs.create false && poetry install --without dev

COPY . .

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
