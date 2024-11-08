import os
import json
from datetime import datetime
from jsonschema import validate, ValidationError

# Класс для хранения информации о файлах
class FileInfo:
    def __init__(self, file_name, full_path, file_size, creation_time, last_modified):
        self.file_name = file_name
        self.full_path = full_path
        self.file_size = file_size
        self.creation_time = creation_time
        self.last_modified = last_modified

    def to_dict(self):
        return {
            "file_name": self.file_name,
            "full_path": self.full_path,
            "file_size": self.file_size,
            "creation_time": self.creation_time,
            "last_modified": self.last_modified
        }

# Сбор информации обо всех файлах в директории data/processed/
def collect_file_info(directory):
    file_infos = []
    for root, _, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            file_info = FileInfo(
                file_name=file,
                full_path=os.path.abspath(file_path),
                file_size=os.path.getsize(file_path),
                creation_time=datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y-%m-%d %H:%M:%S"),
                last_modified=datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
            )
            file_infos.append(file_info.to_dict())
    return file_infos

# Сериализация данных в JSON
def serialize_to_json(data, output_path):
    with open(output_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

# Определение директории для сбора информации
processed_data_dir = os.path.join("project_root", "data", "processed")
output_json_path = os.path.join("project_root", "output", "file_info.json")

# Сбор и сериализация данных
file_info_data = collect_file_info(processed_data_dir)
serialize_to_json(file_info_data, output_json_path)

print(f"Информация о файлах сохранена в {output_json_path}")
