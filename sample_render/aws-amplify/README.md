# AWS Amplify

☁️ **[AWS Amplify](https://aws.amazon.com/amplify/)** - инструменты и сервисы для создания, развертывания и управления облачными приложениями. AWS Amplify интегрируется с различными сервисами AWS и поддерживает множество фреймворков и библиотек.

## Основные функции

- Интеграция с AWS
- Поддержка множества фреймворков
- Создание и развертывание облачных приложений
- Управление облачными приложениями

## Пример настройки `amplify.yml`

```plaintext
version: 1
frontend:
  phases:
    preBuild:
      commands:
        - npm install
    build:
      commands:
        - npm run build
  artifacts:
    baseDirectory: build
    files:
      - '**/*'
  cache:
    paths:
      - node_modules/**/*
```