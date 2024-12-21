# Netlify

🌐 **[Netlify](https://www.netlify.com/)** - это платформа для развертывания статических сайтов и современных веб-приложений. Netlify предлагает функции автоматического билда, развертывания и интеграции с Git для бесшовного CI/CD.

## Основные функции

- Автоматический билд
- Интеграция с Git
- Бесшовный CI/CD

## Пример настройки `netlify.toml`

```plaintext
[build]
  publish = "public"
  command = "jekyll build"

[context.production.environment]
  JEKYLL_ENV = "production"

[context.deploy-preview]
  command = "jekyll build --future"
```