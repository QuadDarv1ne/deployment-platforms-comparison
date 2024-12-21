# DigitalOcean App Platform

🌊 **[DigitalOcean App Platform](https://www.digitalocean.com/products/app-platform/)** - платформа для развертывания, управления и масштабирования приложений с минимальной настройкой. DigitalOcean App Platform предлагает простоту использования и экономичность для разработчиков.

## Основные функции

- Простота использования
- Экономичность
- Масштабирование
- Управление приложениями

## Пример настройки `docker-compose.yml`

```plaintext
version: '3.8'

services:
  app:
    image: node:14
    working_dir: /usr/src/app
    volumes:
      - .:/usr/src/app
    ports:
      - "3000:3000"
    depends_on:
      - mongo
    command: npm start

  mongo:
    image: mongo:latest
    ports:
      - "27017:27017"
    volumes:
      - mongo-data:/data/db

volumes:
  mongo-data:
```