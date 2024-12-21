# Microsoft Azure App Service

🔧 **[Microsoft Azure App Service](https://azure.microsoft.com/services/app-service/)** - платформа для создания, развертывания и масштабирования веб-приложений и API. Azure App Service обеспечивает высокую доступность, автоматическое масштабирование и интеграцию с другими сервисами Azure.

## Основные функции

- Высокая доступность
- Автоматическое масштабирование
- Интеграция с сервисами Azure
- Создание и развертывание веб-приложений и API

## Пример настройки `web.config`

```plaintext
<?xml version="1.0" encoding="utf-8"?>
<configuration>
  <system.webServer>
    <handlers>
      <add name="aspNetCore" path="*" verb="*" modules="AspNetCoreModuleV2" resourceType="Unspecified"/>
    </handlers>
    <aspNetCore processPath="dotnet" arguments=".\MyApp.dll" stdoutLogEnabled="false" stdoutLogFile=".\logs\stdout" hostingModel="InProcess"/>
  </system.webServer>
</configuration>
```