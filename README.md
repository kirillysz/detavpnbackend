# detavpn-backend
## 1. Установка
```bash
git clone https://github.com/kirillysz/detavpnbackend
cd detavpnbackend

chmod +x start.sh
```
## 2. Настройка .env
Создайте файл .env с:
```bash
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=detavpn

DB_USER=postgres
DB_PASSWORD=postgres
DB_NAME=detavpn
DATABASE_URL=postgresql+asyncpg://postgres:postgres@db:5432/detavpn

SECRET_KEY=my_secret
JWT_ALGORITHM=HS256
JWT_EXPIRATION_TIME=3600
```

## 3. Развертывание докера
```bash
docker compose up -d
```

ну вот и все
