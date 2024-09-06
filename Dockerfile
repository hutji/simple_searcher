FROM python:3.11-slim as base

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY pyproject.toml poetry.lock ./
RUN pip install poetry && poetry install --no-dev

COPY . .

CMD ["poetry", "run", "python", "-m", "app.main"]
