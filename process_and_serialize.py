import os
import json
from datetime import datetime

# Определяем пути к директориям
project_root = "project_root"
raw_data_dir = os.path.join(project_root, "data/raw")
processed_data_dir = os.path.join(project_root, "data/processed")
output_dir = os.path.join(project_root, "output")

# Создаем директорию processed, если она еще не существует
os.makedirs(processed_data_dir, exist_ok=True)

# Функция для чтения файла с определением кодировки
def read_file_with_encoding(file_path):
    encodings = ["utf-8", "iso-8859-1", "latin-1"]
    for encoding in encodings:
        try:
            with open(file_path, "r", encoding=encoding) as file:
                return file.read(), encoding
        except UnicodeDecodeError:
            continue
    raise ValueError(f"Не удалось определить кодировку для файла {file_path}")

# Список для хранения информации о обработанных файлах
processed_files_data = []

# Обработка каждого файла в директории raw
for file_name in os.listdir(raw_data_dir):
    raw_file_path = os.path.join(raw_data_dir, file_name)

    # Пропускаем файлы, если это не текстовые файлы
    if not os.path.isfile(raw_file_path):
        continue

    # Чтение содержимого файла
    original_content, encoding = read_file_with_encoding(raw_file_path)

    # Преобразование текста: заглавные буквы -> строчные и наоборот
    transformed_content = original_content.swapcase()

    # Сохранение обработанного содержимого в новый файл в директорию processed
    processed_file_name = f"{os.path.splitext(file_name)[0]}_processed.txt"
    processed_file_path = os.path.join(processed_data_dir, processed_file_name)
    with open(processed_file_path, "w", encoding="utf-8") as processed_file:
        processed_file.write(transformed_content)

    # Сбор информации о обработанном файле
    file_info = {
        "file_name": processed_file_name,
        "original_text": original_content,
        "transformed_text": transformed_content,
        "file_size_bytes": os.path.getsize(processed_file_path),
        "last_modified": datetime.fromtimestamp(os.path.getmtime(processed_file_path)).strftime("%Y-%m-%d %H:%M:%S")
    }
    processed_files_data.append(file_info)

# Сериализация данных в JSON
os.makedirs(output_dir, exist_ok=True)
output_file_path = os.path.join(output_dir, "processed_data.json")
with open(output_file_path, "w", encoding="utf-8") as json_file:
    json.dump(processed_files_data, json_file, indent=4, ensure_ascii=False)

print("Обработка и сериализация данных завершена.")
