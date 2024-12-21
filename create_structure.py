import json
import os

# Чтение данных из JSON файла
with open('data.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# Создание основной директории
base_dir = "sample_render"
os.makedirs(base_dir, exist_ok=True)

# Функция для создания файлов
def create_file(directory, filename, content):
    with open(os.path.join(directory, filename), "w", encoding="utf-8") as file:
        file.write(content)

# Добавление информации о платформах
for platform in data['platforms']:
    platform_dir = os.path.join(base_dir, platform['name'].lower())
    os.makedirs(platform_dir, exist_ok=True)
    create_file(platform_dir, "README.md", f"# {platform['name']}\n\n{platform['description']}\n\n## Основные функции\n\n" + '\n'.join([f"- {feature}" for feature in platform.get('features', [])]))

# Добавление информации об аналогах
for analog in data['analogs']:
    analog_dir = os.path.join(base_dir, analog['name'].lower().replace(" ", "-"))
    os.makedirs(analog_dir, exist_ok=True)
    create_file(analog_dir, "README.md", f"# {analog['name']}\n\n{analog['description']}\n\n## Основные функции\n\n" + '\n'.join([f"- {feature}" for feature in analog.get('features', [])]) + f"\n\n## {analog['example']['title']}\n\n```plaintext\n{analog['example']['code']}\n```")
    create_file(analog_dir, analog['example']['title'].split(' ')[2].replace('`', ''), analog['example']['code'])

print("Структура папок и файлов успешно создана.")