FROM python:3.12-slim

ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/app

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && pip install psycopg2 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "main.wsgi:application", "--bind", "0.0.0.0:8000", "--reload"]