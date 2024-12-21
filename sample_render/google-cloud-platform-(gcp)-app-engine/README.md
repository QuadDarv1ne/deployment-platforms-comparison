# Google Cloud Platform (GCP) App Engine

☁️ **[Google Cloud Platform (GCP) App Engine](https://cloud.google.com/appengine)** - платформа для развертывания и масштабирования приложений на инфраструктуре Google. App Engine предлагает автоматическое масштабирование, интеграцию с другими сервисами GCP и поддержку различных языков программирования.

## Основные функции

- Автоматическое масштабирование
- Интеграция с сервисами GCP
- Поддержка различных языков программирования

## Пример настройки `app.yaml`

```plaintext
runtime: python39

handlers:
  - url: /static
    static_dir: static
  - url: /.*
    script: auto
```