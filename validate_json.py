import json
from jsonschema import validate, ValidationError

# Загрузка JSON Schema
with open("file_info_schema.json", "r", encoding="utf-8") as schema_file:
    schema = json.load(schema_file)

# Загрузка данных для валидации
with open("project_root/output/file_info.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

# Валидация данных
try:
    validate(instance=data, schema=schema)
    print("JSON-файл валиден.")
except ValidationError as e:
    print(f"Ошибка валидации JSON: {e.message}")
