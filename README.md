# detavpn-backend
## 1. Установка
```bash
git clone https://github.com/kirillysz/detavpnbackend
cd detavpnbackend
```
## 2. Настройка .env
Создайте файл .env с:
```bash
DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=db

DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/db
```

## 3. Развертывание докера
```bash
docker compose up -d
```

ну вот и все
