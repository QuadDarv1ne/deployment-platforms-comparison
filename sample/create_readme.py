import json

# Чтение данных из JSON файла
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Формирование содержимого для README.md
readme_content = f"# {data['title']}\n\n"
readme_content += f"{data['introduction']}\n\n"

# Добавление информации о платформах
for platform in data['platforms']:
    readme_content += f"## 🌟 {platform['name']}\n\n"
    readme_content += f"{platform['description']}\n\n"

# Добавление информации об аналогах
readme_content += "## 🔄 Аналоги Amwera и Render\n\n"
for analog in data['analogs']:
    readme_content += f"### ⚙️ {analog['name']}\n\n"
    readme_content += f"{analog['description']}\n\n"
    if 'example' in analog:
        readme_content += f"#### {analog['example']['title']}\n\n"
        readme_content += f"```plaintext\n{analog['example']['code']}\n```\n\n"

# Добавление заключения
readme_content += f"{data['conclusion']}\n\n"

# Добавление информации об авторе
readme_content += "---\n\n"
readme_content += f"**Автор:** {data['author']['name']}\n\n"
readme_content += f"**TG:** {data['author']['tg']}\n\n"
readme_content += f"**Дата:** {data['author']['date']}\n"

# Запись содержимого в файл README.md
with open("README.md", "w", encoding="utf-8") as file:
    file.write(readme_content)

print("Файл README.md успешно создан и сохранен.")