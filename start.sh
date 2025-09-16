#!/bin/sh

until pg_isready -h db -U "$DB_USER"; do
  echo "Waiting for database..."
  sleep 5
done

alembic upgrade head

exec uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload