# GitHub Pages

🛡️ **[GitHub Pages](https://pages.github.com/)** - сервис для хостинга статических сайтов прямо из GitHub-репозиториев. GitHub Pages поддерживает автоматическое развертывание при пуше в репозиторий и интеграцию с Jekyll для генерации статических сайтов.

## Основные функции

- Хостинг статических сайтов
- Автоматическое развертывание
- Интеграция с Jekyll

## Пример настройки `_config.yml`

```plaintext
title: My Awesome Site
description: >- # this means to ignore newlines until "baseurl:"
  Welcome to my awesome site. This is the place where I share my projects and ideas.
baseurl: "" # the subpath of your site, e.g. /blog
url: "https://yourusername.github.io" # the base hostname & protocol for your site
theme: minima

# Build settings
markdown: kramdown
```