FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt . 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

WORKDIR /app

CMD ["sh", "-c", "cd app && uvicorn app:app --host 0.0.0.0 --port 8000"]